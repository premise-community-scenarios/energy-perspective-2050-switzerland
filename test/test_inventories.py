from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from schema import And, Optional, Or, Schema, Use

from .ecoinvent_modification import (
    LIST_IMAGE_REGIONS,
    LIST_REMIND_REGIONS,
    SUPPORTED_EI_VERSIONS,
)
from .transformation import *
from .utils import eidb_label


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

            for i, a in enumerate(data):
                a["custom scenario dataset"] = True

                if (name, ref) == (a["name"], a["reference product"]):
                    data[i] = flag_activities_to_adjust(
                        a, df, model, pathway, v, custom_data
                    )

    return data
