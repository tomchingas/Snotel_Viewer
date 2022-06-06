# Project Mission 

The intention of this project is to create a webapp that allows the user to view a map of the US which displays all the active NRCS Snotel sites. The user will be able to select a site and view the data associated with that gage. 

# General build informaiton

Framework - Django 4.0.1
Database - Docker container running PostgresSQL and PostGIS (stored locally for now)

UPDATE AS NEEDED

# Data references (USDA NRCS NWCC Report Generator)

## Webpage the station metadata was created from:
https://wcc.sc.egov.usda.gov/reportGenerator/view/customMultiTimeSeriesGroupByStationReport/daily/start_of_period/network=%22SNTL%22%20AND%20outServiceDate=%222100-01-01%22%7Cname/0,0/name,stationId,state.code,state.name,network.code,network.name,elevation,latitude,longitude,county.name,county.code,huc2.huc,huc2.hucName,huc4.huc,huc4.hucName,huc6.huc,huc6.hucName,huc8.huc,huc8.hucName,huc10.huc,huc10.hucName,huc12.huc,huc12.hucName,reportTimeZone.offset,dco.code,actonId,shefId,inServiceDate,outSer

## Main webpage for data request for particular snotel gage:
https://wcc.sc.egov.usda.gov/reportGenerator/#

## Example of data request:
https://wcc.sc.egov.usda.gov/reportGenerator/view_csv/customMultiTimeSeriesGroupByStationReport/hourly/start_of_period/301:CA:SNTL%7Cid=%22%22%7Cname/0,0/WTEQ::value?fitToScreen=false

# Build References

## Docker container with PostgresSQL and PostGIS:
https://github.com/kartoza/docker-postgis

## General framework/database set up:
https://realpython.com/location-based-app-with-geodjango-tutorial/

##UPDATE AS NEEDED

# How to run the app

## Current build info:
The app is currently only setup to run locally. A '.env' file is used to store information that shouldn't be uploaded to github. The docker container containing the databases is currently only stored locally on my machine. To make this work a new user would need to create their own docker container and populate the database (see build references).

## Follow these steps to run the app locally:

### Ensure the docker container is running:
$ sudo docker ps -a

$ sudo docker start -i <name/id>

### Create a virtual python environment, activate the virtual environment, and install required python libraries
(env) $ pip install -r requirments.txt

### Run the django server
.../SnotelViewer$ python manage.py runserver
