from kafka import KafkaConsumer
from api import logger, global_settings
from dotenv import load_dotenv
import os
import json
import requests
from threading import Thread
from .es_job import create_logger

load_dotenv()


# poetry add kafka-python
def consumer_kafka(doc, topic):
    # brokers = ['localhost:29092', 'localhost:39092']
    # topics = 'test-topic'
    # brokers = str(os.getenv("KAFKA_HOST", doc['app']['kafka']['host'])).split(",")
    
    consumer = KafkaConsumer(topic, group_id="Python_Kafka_Consumer_Job", bootstrap_servers=global_settings.get_Kafka_Hosts())
    for message in consumer:
        logger.info("{}, {}, {}".format(message, message.value, message.value.decode("utf-8")))
        
        '''
        docs = [{'index': {'_index': 'Kafka_Indexing'}}]
        docs.append(json.loads(message.value.decode("utf-8")))
        # Buffer = [str(each_row).replace("'", '"') + '\n' for doc in docs for each_row in doc]
        print('@#$$$', docs, type(docs))

        URL = 'http://localhost:9209/_bulk'
        headers = {'Content-Type': 'application/x-ndjson', 'Authorization': 'Basic ZWxhc3RpYzpnc2FhZG1pbg=='}
        response = requests.post(URL, headers=headers, data="\n".join(docs).encode('utf-8'), timeout=30000)
        print(response.status_code)
        print(response.text)
        '''
        create_logger(message.value.decode("utf-8"))
    
    logger.info("-- job finished..--")
