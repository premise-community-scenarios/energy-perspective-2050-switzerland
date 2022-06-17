# energy-perspective-2050-switzerland ![GitHub release (latest by date)](https://img.shields.io/github/v/release/premise-community-scenarios/energy-perspective-2050-switzerland) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6653949.svg)](https://doi.org/10.5281/zenodo.6653949)


Description
-----------

This is a repository containing a scenario that implements the projections of the 
Energy Perspective 2050+ report for:

* electricity, 
* hydrogen, 
* gas, 
* and liquid fuels. 

It is meant to be used in `premise` in addition to a global IAM scenario, to provide 
refined projections at the country level.

This data package contains all the files necessary for `premise` to implement
this scenario and create market-specific composition for electricity (including imports from
neighboring countries), liquid and gaseous fuels (including hydrogen).

Sourced from publication
------------------------

Energy perspectives 2050+\
Swiss Federal Office for Energy\
https://www.bfe.admin.ch/bfe/en/home/policy/energy-perspectives-2050-plus.html/

Data validation 
---------------

[![goodtables.io](https://goodtables.io/badge/github/premise-community-scenarios/energy-perspective-2050-switzerland.svg)](https://goodtables.io/github/premise-community-scenarios/energy-perspective-2050-switzerland)

Test 
----

![example workflow](https://github.com/premise-community-scenarios/energy-perspective-2050-switzerland/actions/workflows/main.yml/badge.svg?branch=main)

Ecoinvent database compatibility
--------------------------------

ecoinvent 3.8 cut-off

IAM scenario compatibility
---------------------------

The following coupling is done between IAM and EP2050+ scenarios:

* IMAGE SSP2-Base (-> EP2050+ Business As Usual)
* IMAGE SSP2-RCP26 (-> EP2050+ ZERO Basis)
* REMIND SSP2-Base (-> EP2050+ Business As Usual)
* REMIND SSP2-PkBudg1100 (-> EP2050+ ZERO Basis)
* REMIND SSP2-PkBudg900 (-> EP2050+ ZERO Basis)

What does this add?
-------------------

This external scenario creates the markets listed below according
to the projections from the Energy Perspectives 2050+.

* `market for electricity, high voltage, EP2050` (CH)
* `market for electricity, medium voltage, EP2050` (CH)
* `market for electricity, medium voltage, EP2050` (CH)
* `import from neighboring countries, high voltage` (CH)

These markets are relinked to activities that consume electricity in Switzerland.

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
                ep2050, # <-- list datapackages here
            ] 
        )
```

