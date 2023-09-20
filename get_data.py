import os
import requests
import pandas as pd

def get_source_ids(municipalities = ['Hamar']):
    
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

def get_sensor_data(observation_locations, measurement_types):

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

municipalities = ['Hamar', 'Ringsaker', 'Stange']
measurements = 'mean(air_temperature P1D),sum(precipitation_amount P1D),mean(wind_speed P1D)'
observation_ids = get_source_ids(municipalities)
get_sensor_data(observation_ids, measurements)



