import pandas as pd
import yaml


def check_inventories(custom_scenario, data, model, pathway, custom_data):

    for i, scenario in enumerate(custom_scenario):

        with open(scenario["config"], "r") as stream:
            config_file = yaml.safe_load(stream)

        df = pd.read_excel(scenario["scenario data"])

        for k, v in config_file["production pathways"].items():

            name = v["ecoinvent alias"]["name"]
            ref = v["ecoinvent alias"]["reference product"]

            if (
                len(
                    [
                        a
                        for a in data
                        if (name, ref) == (a["name"], a["reference product"])
                    ]
                )
                == 0
            ) and not v["ecoinvent alias"].get("exists in ecoinvent"):
                raise ValueError(
                    f"The inventories provided do not contain the activity: {name, ref}"
                )

    return data
