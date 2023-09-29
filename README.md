# Weather Forecast
Predicting weather using yr.no's API.

The API references can be found here: https://frost.met.no/api.html
## Setting up

* In order to start using the API you have to create a free user at https://frost.met.no/auth/requestCredentials.html
Follow the instructions and recieve a client id

* Clone this repo and create a new conda environment using the included .yaml file:

  ```conda create env -f <env-file.yaml>```

* Export the client_id as an environment variable:

  ```conda env config vars set client_id = <client_id from yr registration>```

* Deactivate and reactivate the conda env and you're good to go!


## Schedule runs

* In order to schedule scripts to run at set times, one can use either cron jobs on linux systems or task scheduler on windows (very simple).
* create a new task and set it up to point at 1. the python.exe being used (type where python to get all locations in venvs as well). and 2. full path to the script that is going to be scheduled.
