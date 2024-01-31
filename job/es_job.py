
from elasticsearch import Elasticsearch
from dotenv import load_dotenv
from api import logger
import json

load_dotenv()

def get_headers():
    ''' Elasticsearch Header '''
    return {'Content-type': 'application/json', 'Authorization': 'Basic ZWxhc3RpYzpnc2FhZG1pbg==', 'Connection': 'close'}

def es_instance():    
    es_client = Elasticsearch(hosts="http://localhost:9209", headers=get_headers(), timeout=600)
    return es_client
    
    
def create_logger(message):
    es_client = es_instance()
    response = es_client.index(index='kafka_indexing', body=json.loads(message))
    logger.info(response)
        