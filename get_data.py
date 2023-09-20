import os
import requests
import pandas as pd

def get_source_ids(municipalities = ['Hamar']):
    
    endpoint_sources = 'https://frost.met.no/sources/v0.jsonld'
    
    for i, municipality in enumerate(municipalities):
        
        source_parameters = {
            'municipality' : municipalities[i],
        }
        
        r = requests.get(endpoint_sources, source_parameters, auth=(os.getenv('client_id'),''))
        
        source_response = r.json()

        for datapoint in source_response['data']:
            print(datapoint['name'], datapoint['id'])
    

municipalities = ['Hamar', 'Ringsaker', 'Stange']

get_source_ids(municipalities)



