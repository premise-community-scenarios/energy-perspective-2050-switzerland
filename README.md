# energy-perspective-2050-switzerland ![GitHub release (latest by date)](https://img.shields.io/github/v/release/premise-community-scenarios/energy-perspective-2050-switzerland) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6653948.svg)](https://doi.org/10.5281/zenodo.6653948)


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

| IAM scenario           | EP2050+ scenario     |
|------------------------|----------------------|
| IMAGE SSP2-Base        | Business As Usual    |
| IMAGE SSP2-RCP26       | ZERO Basis (default) |
| IMAGE SSP2-RCP26       | ZERO A               |
| IMAGE SSP2-RCP26       | ZERO B               |
| IMAGE SSP2-RCP26       | ZERO C               |
| IMAGE SSP2-RCP19       | ZERO Basis (default) |
| IMAGE SSP2-RCP19       | ZERO A               |
| IMAGE SSP2-RCP19       | ZERO B               |
| IMAGE SSP2-RCP19       | ZERO C               |
| REMIND SSP2-Base       | Business As Usual    |
| REMIND SSP2-PkBudg1150 | ZERO Basis (default) |
| REMIND SSP2-PkBudg1150 | ZERO A               |
| REMIND SSP2-PkBudg1150 | ZERO B               |
| REMIND SSP2-PkBudg1150 | ZERO C               |
| REMIND SSP2-PkBudg500  | ZERO Basis           |
| REMIND SSP2-PkBudg500  | ZERO A               |
| REMIND SSP2-PkBudg500  | ZERO B               |
| REMIND SSP2-PkBudg500  | ZERO C               |

What does this do?
------------------

![map electricity markets](assets/map.png)

This external scenario creates markets for Switzerland listed below, according
to the projections from the Energy Perspectives 2050+ (yellow boundaries in map above).

Electricity
***********

* `market for electricity, high voltage, EP2050` (CH)
* `market for electricity, medium voltage, EP2050` (CH)
* `market for electricity, medium voltage, EP2050` (CH)

These markets are relinked to activities that consume electricity in Switzerland.

Additionally, the Swiss markets rely to a varying extent on imports from
neighboring countries (FR + DE + IT + AT), for which a market is also created 
(orange boundaries in map above):

* `import from neighboring countries electricity, high voltage` (CH)

That market itself relies on imports from the rest of Europe, which is
provided by the regional IAM market for European electricity (blue boundaries in map above).

Liquid fuels
************

* `market for petrol, EP2050` (CH)
* `market for diesel, EP2050` (CH)

This includes the production of biofuel and synthetic fuel.
The latter is produced in the neighboring countries, using
the corresponding markets for hydrogen and electricity.


Gaseous fuels
*************

* `market for hydrogen, gaseous, EP2050` (CH)
* `market for compressed gas, high pressure, EP2050` (CH)
* `market for compressed gas, low pressure, EP2050` (CH)

For hydrogen, this includes the domestic and foreign production, via electrolysis.
The latter is produced in the neighboring countries, using
the corresponding markets for electricity.

For compressed gas, this includes the provision of natural gas, biomethane
and synthetic gas (from neighboring countries), using
the corresponding markets for electricity.

How are technologies mapped?
---------------------------
The tables below show how the mapping between reported technologies
and LCI datasets is done. Unless specified otherwise, ecoinvent
LCI datasets are used.

Electricity
***********

| Technologies in EP2050+            | LCI datasets used                                               | Remarks                                                                                                                   |
| ---------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Hydro, run-of-river                | electricity production, hydro, run-of-river                     |
| Hydro, alpine reservoir            | electricity production, hydro, reservoir, alpine region         |
| Nuclear, Boiling water reactor     | electricity production, nuclear, boiling water reactor          | The split between boiling water and pressure water is not provided. We use the current split, based on production volume. |
| Nuclear, Pressure water reactor    | electricity production, nuclear, pressure water reactor         |
| Conventional, Waste-to-Energy      | treatment of municipal solid waste, incineration                |
| Conventional, Other                | electricity production, natural gas, combined cycle power plant | The report does not specify what "Other" is. Assumed to be natural gas.                                                   |
| Conventional, Coal                 | electricity production, hard coal                               |
| Conventional, Natural gas          | electricity production, natural gas, combined cycle power plant |
| Renewable, Photovoltaic            | electricity production, photovoltaic                            | Datasets from 10.13140/RG.2.2.17977.19041.                                                                                |
| Renewable, Wind turbines, Onshore  | electricity production, wind, 1-3MW turbine, onshore            |
| Renewable, Wind turbines, Offshore | electricity production, wind, 1-3MW turbine, offshore           |
| Renewable, Geothermal              | electricity production, deep geothermal                         | Dataset provided by premise, based on the geothermal heat dataset of ecoinvent.                                           |
| Renewable, Biomass                 | heat and power co-generation, wood chips, 6667 kW               |
| Renewable, Biogas                  | heat and power co-generation, biogas, gas engine                |

Liquid fuels
************


| Technologies in EP2050+            | LCI datasets used                                               | Remarks                                                                                                             |
|------------------------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Diesel                             | market for diesel, low-sulfur                                   | 
| Biodiesel                          | Biodiesel, from rapeseed oil, at fuelling station         | Provided by premise. |
| Synthetic diesel                   | diesel production, synthetic, from Fischer Tropsch process, hydrogen from electrolysis, energy allocation, at fuelling station, EP2050          | Provided by premise. |
| Petrol                             | market for petrol, low-sulfur                                   |
| Bioethanol                         | ethanol production from sugar beet                |
| Synthetic petrol                   | gasoline production, synthetic, from methanol, hydrogen from electrolysis, CO2 from DAC, energy allocation, at fuelling station, EP2050 | Provided by premise. |                                                                                                |



Gaseous fuels
*************


| Technologies in EP2050+ | LCI datasets used                                                                                                                      | Remarks          |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Hydrogen, domestic      | hydrogen production, electrolysis, 25 bar, domestic, EP2050                                                                            | Provided by premise. |
| Hydrogen, imported      | hydrogen production, electrolysis, 25 bar, imported, EP2050                                                                            | Provided by premise. |
| Compressed natural gas  | natural gas, high pressure, at consumer | From 10.13140/RG.2.2.29142.78409.           |
| Liquefied natural gas   | market for natural gas, liquefied                                                                                                          |
| Biomethane              | market for biomethane, high pressure                                                                                                          |
| Synthetic gas           | Methane, synthetic, gaseous, 5 bar, from electrochemical methanation, at fuelling station, EP2050 | Provided by premise. |



Flow diagram
------------

![map electricity markets](assets/flow_diagram.png)

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
                {"model":"image", "pathway":"SSP2-Base", "year":2050, "external scenarios": [{"scenario": "Business As Usual", "data": ep2050}]},
                {"model":"image", "pathway":"SSP2-RCP26", "year":2030, "external scenarios": [{"scenario": "ZERO Basis", "data": ep2050}]},
            ],        
            source_db="ecoinvent 3.8 cutoff",
            source_version="3.8",
            key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        )
    ndb.update_external_scenario()
```

