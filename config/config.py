import os

class Settings:
    def __init__(self, logger, doc):
        self.logger = logger
        self.doc = doc
        
        # Read_Doc with arguments from Docker -e option
        self.hosts: str = os.getenv("ES_HOST", doc['app']['es']['es_host'])
        self.index: str = os.getenv("ES_LOGGER_INDEX", doc['app']['es']['index']['index'])
        
        self.kafka_hosts = str(os.getenv("KAFKA_HOST", doc['app']['kafka']['host'])).split(",")
        self.kafka_topics = str(os.getenv("KAFKA_TOPIC", doc['app']['kafka']['topic'])).split(",")
        
        self.logger.info(f'@@elasticsearch.hosts - {self.hosts}, elasticsearch.index : {self.index}, kafka_hosts : {self.kafka_hosts},')

        
    def get_Hosts(self):
        return self.hosts
    
    def get_es_index(self):
        return self.index
    
    def get_Kafka_Hosts(self):
        return self.kafka_hosts
    
    def get_Kafka_topic(self):
        return self.kafka_topics
    