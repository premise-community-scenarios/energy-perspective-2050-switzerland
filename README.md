# energy-perspective-2050-switzerland ![GitHub release (latest by date)](https://img.shields.io/github/v/release/premise-community-scenarios/energy-perspective-2050-switzerland) [![DOI](https://zenodo.org/badge/496564841.svg)](https://zenodo.org/badge/latestdoi/496564841)


Description
-----------

This is a repository containing a scenario that implements the projection of the Energy Perspective 2050+ report for electricity, hydrogen, gas and liquid fuels.

This is a data package that contains all the files necessary for premise to implement
this scenario and create market-specific composition for electricity (including imports from
neighboring countries), liquid and gaseous fuels (including hydrogen).

Sourced from publication
------------------------

Energy perspectives 2050+
Swiss Federal Office for Energy
https://www.bfe.admin.ch/bfe/en/home/policy/energy-perspectives-2050-plus.html/

Data validation 
---------------

Goodtables.io [![goodtables.io](https://goodtables.io/badge/github/premise-community-scenarios/energy-perspective-2050-switzerland.svg)](https://goodtables.io/github/premise-community-scenarios/energy-perspective-2050-switzerland)

Test 
----

GitHubAction ![example workflow](https://github.com/premise-community-scenarios/energy-perspective-2050-switzerland/actions/workflows/main.yml/badge.svg?branch=main)


Ecoinvent database compatibility
--------------------------------

ecoinvent 3.8 cut-off

IAM scenario compatibility
---------------------------

Compatible with the following IAM scenarios:
* IMAGE SSP2-Base
* IMAGE SSP2-RCP26
* IMAGE SSP2-RCP19
* REMIND SSP2-Base
* REMIND SSP2-PkBudg1300
* REMIND SSP2-PkBudg1100
* REMIND SSP2-PkBudg900

How to use it?
--------------

```python

    import brightway2 as bw
    from premise import NewDatabase
    from datapackage import Package
    
    
    fp = r"https://raw.githubusercontent.com/premise-community-scenarios/energy-perspective-2050-switzerland/main/datapackage.json"
    ep2050 = Package(fp)
    
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
                ep2050, # <-- list datapackage objects here
            ] 
        )
```

