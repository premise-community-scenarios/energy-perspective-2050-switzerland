# scenario-example-bread [![goodtables.io](https://goodtables.io/badge/github/premise-community-scenarios/scenario-example-bread.svg)](https://goodtables.io/github/premise-community-scenarios/scenario-example-bread) ![example workflow](https://github.com/premise-community-scenarios/scenario-example-bread/actions/workflows/main.yml/badge.svg?branch=main) [![DOI](https://zenodo.org/badge/496564841.svg)](https://zenodo.org/badge/latestdoi/496564841)

Description
-----------

This is an example of a repository containing a custom prospective scenario for breadmaking, to be used in premise.
This is a data package that contains all the files necessary for premise to implement
this custom scenario. This is a dummy scenario to illustrate the principle of custom scenarios and their use alongside IAM scenarios.

Sourced from publication
------------------------

None

Ecoinvent database compatibility
--------------------------------

ecoinvent 3.8 cut-off

IAM scenario compatibility
---------------------------

Compatible with the following IAM scenarios:
* IMAGE SSP2-Base
* IMAGE SSP2-RCP26

How to use it?
--------------

```python

    import brightway2 as bw
    from premise import NewDatabase
    from datapackage import Package
    
    
    fp = r"https://raw.githubusercontent.com/premise-community-scenarios/scenario-example-bread/main/datapackage.json"
    bread_scenario = Package(fp)
    
    bw.projects.set_current("your_bw_project")
    
    ndb = NewDatabase(
            scenarios = [
                {"model":"image", "pathway":"SSP2-Base", "year":2050,},
                {"model":"image", "pathway":"SSP2-RCP26", "year":2030,},
            ],        
            source_db="ecoinvent 3.8 cutoff",
            source_version="3.8",
            key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            custom_scenario=[
                bread_scenario, # <-- list datapackage objects here
            ] 
        )
```

