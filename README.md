# Weather Forecast
Predicting weather.
Get data using yr.no's API.

The API references can be found here: https://frost.met.no/api.html
## Setting up

* In order to start using the API you have to create a free user at https://frost.met.no/auth/requestCredentials.html
Follow the instructions and recieve a client id

* Clone this repo and create a new conda environment using the included .yaml file:

  ```conda create env -f <env-file.yaml>```

* Export the client_id as an environment variable:

  ```conda env config vars set client_id = <client_id from yr registration>```

* Deactivate and reactivate the conda env and you're good to go!


## Scheduled runs

Because it is difficult to fetch historical radar image data from yr.no, we can schedule the get_data.py script to fetch data every hour (smallest temporal increment for images).

1. run task scheduler on windows (easiest option)

2. create new task, specify how often it should run.

3. Specify full path to python executable (find the paths by typing in "where python" in the terminal shell)

4. In the "Add arguments (optional)" field, sepcify the full path to the script file. 

5. Click done, it will run as often as specified in the setup!  
