import os
import requests
import pandas as pd
from datetime import datetime, timedelta


class GetData:

    def __init__(self):
        return


    def get_source_ids(self, municipalities = ['Hamar']):
        """Takes a list of municipalities as input, returns a list of source IDs for every measuring point in that municipality"""

        endpoint_sources = 'https://frost.met.no/sources/v0.jsonld'
        
        source_ids = []

        for municipality in municipalities:

            source_parameters = {
                'municipality' : municipality,
                'types' : 'SensorSystem'
            }
            
            response = requests.get(endpoint_sources, source_parameters, auth=(os.getenv('client_id'),''))
            
            source_response = response.json()

            for datapoint in source_response['data']:
                print(datapoint['name'], datapoint['id'])
                source_ids.append(datapoint['id'])

        return source_ids

    def get_sensor_data(self, observation_locations = [], measurement_types = ""):
        """Takes a list of measurement stations IDs and a string of measurement types as input, returns all measurement data from given locations and measurement types as a single dataframe."""

        endpoint_observations = 'https://frost.met.no/observations/v0.jsonld'

        df = pd.DataFrame()

        for location in observation_locations:
            observation_parameters = {
                'sources' : location,
                'elements' : measurement_types,
                'referencetime' : '2023-09-01/2023-09-20',
                'performancecategories' : 'A,B,C'
            }

            response = requests.get(endpoint_observations, observation_parameters, auth=(os.getenv('client_id'),''))

            observation_response = response.json()['data']
            #print(observation_response[0]['referenceTime'], len(observation_response[0]['observations']))

            for observation in observation_response:
                
                single_observation = pd.DataFrame(observation['observations'])
                
                single_observation['referenceTime'] = observation['referenceTime']
                single_observation['sourceId'] = observation['sourceId']
                df = pd.concat([df, single_observation])
                
        print(df.head(50))
        return df

    def get_image_data(self, type, region, month, day, hour, savefile_path):
        """type = type of measurement, region = region in norway to focus on, month (has to be zero-padded), day (has to be zero-padded), hour (has to be zero-padded), savefile_path = save locaiton path.
        returns a png-image"""

        url = 'https://api.met.no/weatherapi/radar/2.0/?type={}&area={}&time=2023-{}-{}T{}:00:00Z'.format(type, region, month, day, hour)
        
        radar_image = requests.get(url)
        
        with open(savefile_path+"radar_image_{}_{}_2023{}{}-{}00.png".format(type, region, month, day, hour), "wb") as f:
            for chunk in radar_image:
                f.write(chunk)

