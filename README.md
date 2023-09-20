# Weather Forecast
Predicting weather using yr.no's API.

The API references can be found here: https://frost.met.no/api.html
## Retrieving data

* In order to start using the API you have to create a free user at https://frost.met.no/auth/requestCredentials.html
Follow the instructions and recieve a client id

* Clone this repo and create a new conda environment using the included .yaml file.

* Export the client_id as an environment variable:

  ```conda env config vars set client_id = <client_id from yr registration>```

* Deactivate and reactivate the conda env and you're good to go!


