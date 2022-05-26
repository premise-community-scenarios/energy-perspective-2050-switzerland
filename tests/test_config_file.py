import yaml
from schema import And, Optional, Or, Schema, Use
from datapackage import Package

from premise.ecoinvent_modification import (
    LIST_IMAGE_REGIONS,
    LIST_REMIND_REGIONS,
    SUPPORTED_EI_VERSIONS,
)

FILEPATH_DATAPACKAGE_SCHEMA = "./datapackage.json"

def test_config_file():

    dp = Package(FILEPATH_DATAPACKAGE_SCHEMA)

    for resource in dp.resources:
        if resource.name == "config":
            with open(resource.descriptor["path"], "r") as stream:
                config_file = yaml.safe_load(stream)
            break

    file_schema = Schema(
        {
            "production pathways": {
                str: {
                    "production volume": {
                        "variable": str,
                    },
                    "ecoinvent alias": {
                        "name": str,
                        "reference product": str,
                        Optional("exists in ecoinvent"): bool,
                    },
                    Optional("efficiency"): [
                        {
                            "variable": str,
                            Optional("reference year"): And(
                                Use(int), lambda n: 2005 <= n <= 2100
                            ),
                            Optional("includes"): {
                                Optional("technosphere"): list,
                                Optional("biosphere"): list,
                            },
                        }
                    ],
                    Optional("except regions"): And(
                        list,
                        Use(list),
                        lambda s: all(
                            i in LIST_REMIND_REGIONS + LIST_IMAGE_REGIONS for i in s
                        ),
                    ),
                    Optional("replaces"): [{"name": str, "reference product": str}],
                    Optional("replaces in"): [
                        {"name": str, "reference product": str}
                    ],
                    Optional("replacement ratio"): float,
                },
            },
            Optional("markets"): [
                {
                    "name": str,
                    "reference product": str,
                    "unit": str,
                    "includes": [{"name": str, "reference product": str}],
                    Optional("except regions"): And(
                        list,
                        Use(list),
                        lambda s: all(
                            i in LIST_REMIND_REGIONS + LIST_IMAGE_REGIONS for i in s
                        ),
                    ),
                    Optional("replaces"): [{"name": str, "reference product": str}],
                    Optional("replaces in"): [
                        {"name": str, "reference product": str}
                    ],
                    Optional("replacement ratio"): float,
                }
            ],
        }
    )

    file_schema.validate(config_file)

    if "markets" in config_file:
        # check that providers composing the market
        # are listed

        for market in config_file["markets"]:

            market_providers = [
                (a["name"], a["reference product"]) for a in market["includes"]
            ]

            listed_providers = [
                (
                    a["ecoinvent alias"]["name"],
                    a["ecoinvent alias"]["reference product"],
                )
                for a in config_file["production pathways"].values()
            ]

            if any([i not in listed_providers for i in market_providers]):
                raise ValueError(
                    "One of more providers listed under `markets/includes` is/are not listed "
                    "under `production pathways`."
                )


def get_recursively(search_dict, field):
    """Takes a dict with nested lists and dicts,
    and searches all dicts for a key of the field
    provided.
    """
    fields_found = []

    for key, value in search_dict.items():

        if key == field:
            fields_found.append(value)

        elif isinstance(value, dict):
            results = get_recursively(value, field)
            for result in results:
                fields_found.append(result)

        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    more_results = get_recursively(item, field)
                    for another_result in more_results:
                        fields_found.append(another_result)

    return fields_found

