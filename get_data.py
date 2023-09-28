import os
import requests
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime, timedelta




def get_source_ids(municipalities = ['Hamar']):
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

def get_sensor_data(observation_locations = [], measurement_types = ""):
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

def get_image_data(type, region, month, day, hour):

    url = 'https://api.met.no/weatherapi/radar/2.0/?type={}&area={}&time=2023-{}-{}T{}:00:00Z'.format(type, region, month, day, hour)
    print('/n'+url)
    radar_image = requests.get(url)
    
    with open("radar_image_{}_{}_2023{}{}-{}h.png".format(type, region, month, day, hour), "wb") as f:
        for chunk in radar_image:
            f.write(chunk)

    #
    #image = plt.imshow(radar_image)
    #plt.show()
    
#while (datetime.now().minute > 00 and 
currentDay = str(datetime.now().strftime('%d'))
currentHour = str((datetime.now()- timedelta(hours=2)).strftime('%H'))
currentMonth = datetime.now().strftime('%m')

get_image_data('accumulated_01h','eastern_norway', currentMonth, currentDay, currentHour)

"""
municipalities = ['Hamar', 'Ringsaker', 'Stange']
measurements = 'mean(air_temperature P1D),sum(precipitation_amount P1D),mean(wind_speed P1D)'
observation_ids = get_source_ids(municipalities)
get_sensor_data(observation_ids, measurements)
"""