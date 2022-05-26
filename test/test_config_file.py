import yaml
from schema import And, Optional, Or, Schema, Use

from premise.ecoinvent_modification import (
    LIST_IMAGE_REGIONS,
    LIST_REMIND_REGIONS,
    SUPPORTED_EI_VERSIONS,
)

def check_config_file(custom_scenario):

    for i, scenario in enumerate(custom_scenario):
        with open(scenario["config"], "r") as stream:
            config_file = yaml.safe_load(stream)

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

    needs_imported_inventories = [False for _ in custom_scenario]

    for i, scenario in enumerate(custom_scenario):
        with open(scenario["config"], "r") as stream:
            config_file = yaml.safe_load(stream)

        if len(list(config_file["production pathways"].keys())) != sum(
            get_recursively(config_file["production pathways"], "exists in ecoinvent")
        ):
            needs_imported_inventories[i] = True

    return sum(needs_imported_inventories)

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

