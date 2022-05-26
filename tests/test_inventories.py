import yaml
import bw2io
from datapackage import Package

FILEPATH_DATAPACKAGE_SCHEMA = "./datapackage.json"
dp = Package(FILEPATH_DATAPACKAGE_SCHEMA)

for resource in dp.resources:
    if resource.name == "inventories":
        i = bw2io.CSVImporter(resource.descriptor["path"])

    if resource.name == "config":
        with open(resource.descriptor["path"], "r") as stream:
            config_file = yaml.safe_load(stream)

def test_length():
    assert len(i.data) > 0


def test_inventories():

    for k, v in config_file["production pathways"].items():

        name = v["ecoinvent alias"]["name"]
        ref = v["ecoinvent alias"]["reference product"]

        if (
            len(
                [
                    a
                    for a in i.data
                    if (name, ref) == (a["name"], a["reference product"])
                ]
            )
            == 0
        ) and not v["ecoinvent alias"].get("exists in ecoinvent"):
            raise ValueError(
                f"The inventories provided do not contain the activity: {name, ref}"
            )

