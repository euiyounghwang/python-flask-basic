
import pytest
from elasticsearch.client import Elasticsearch, IndicesClient
import json



# @pytest.fixture(scope="session")
def test_elasticsearch(mock_es_client):
    # ES 7 will be on 9200 and setup basic index with some datas into local elasticsearch cluster
    assert mock_es_client is not None

    es = mock_es_client

    # ic = IndicesClient(mock_es_client)
    # IndicesClient is equal to es.indices
    ic = es.indices

    def try_delete_index(index):
        try:
            if ic.exists(index):
                # print('Delete index : {}'.format(index))
                ic.delete(index)
        # except NotFoundError:
        except Exception as ex:
            pass
    try_delete_index("test_ngram_v1")
    try_delete_index("test_performance_metrics_v1")

    def create_index(index, def_file_name):
        from os.path import dirname
        # print(open(dirname(__file__) + def_file_name))
        with open(dirname(__file__) + def_file_name) as f:
            index_def = f.read()
        ic.create(index, index_def)
    create_index("test_ngram_v1", "/test_mapping/search_ngram_mapping.json")
    create_index("test_performance_metrics_v1", "/test_mapping/performance_metrics_mapping.json")

    # ngram index
    es.index(index="test_ngram_v1", id=111, body={
            "title": " The quick brown fox jumps over the lazy dog"
        }
    )

    def create_alias(index, name):
        ic.put_alias(index, name)

    es.index(index="test_performance_metrics_v1", id=111, body={
        "title" :  "performance",
        "elapsed_time": 0.3,
        "sequence": 1,
        "entity_type": "performance",
        "env" :  "dev",
        "concurrent_users" :  "20",
        "search_index" :  "test_performance_metrics_v1",
        "@timestamp" : "2023-01-01 00:00:00"
        }
    )
    # es.index(index="test_performance_metrics_v1", id=222, body={
    #     "title" :  "performance",
    #     "elapsed_time": 0.1,
    #     "sequence": 2,
    #     "entity_type": "performance",
    #     "env" :  "dev",
    #     "concurrent_users" :  "20",
    #     "search_index" :  "test_performance_metrics_v1",
    #     "@timestamp" : "2023-01-01 00:00:01"
    #     }
    # )
    
    create_alias("test_performance_metrics_v1", "metrics_search")
    
     # refresh
    es.indices.refresh(index="test_ngram_v1")
    es.indices.refresh(index="test_performance_metrics_v1")


def test_indics_analyzer_elasticsearch(mock_es_client):
    assert mock_es_client is not None

    es = mock_es_client
    ic = es.indices
    response = ic.analyze(
        index="test_ngram_v1",
        body={
            "analyzer": "autocomplete",
            "text": "The quick",
        }
    )
    
    assert response is not None
    # the should be stopword
    assert response == {
        "tokens":[
            {
                "token":"th",
                "start_offset":0,
                "end_offset":2,
                "type":"word",
                "position":0
            },
            {
                "token":"qu",
                "start_offset":4,
                "end_offset":6,
                "type":"word",
                "position":2
            },
            {
                "token":"qui",
                "start_offset":4,
                "end_offset":7,
                "type":"word",
                "position":3
            },
            {
                "token":"quic",
                "start_offset":4,
                "end_offset":8,
                "type":"word",
                "position":4
            },
            {
                "token":"quick",
                "start_offset":4,
                "end_offset":9,
                "type":"word",
                "position":5
            }
        ]
    }


def test_search_elasticsearch(mock_es_client):
    assert mock_es_client is not None

    es = mock_es_client

    response = es.get(index="test_performance_metrics_v1", id=111)
    print(response)
    assert response is not None
    assert '_source' in response and response['_source']['title'] == 'performance'

    query = {
        "query": {
            "match": {
                "title": "performance"
            }
        }
    }

    # query_string
    # query = {
    #     "query": {
    #         "query_string": {
    #             "fields": ['title^3'],
    #            "default_operator": "AND",
    #             "analyzer": "standard",
    #             "query": "performance"
    #         }
    #     }
    # }

    response = es.search(index="test_performance_metrics_v1", body=query)
    assert response is not None
    assert response['hits']['total']['value'] > 0
    # print(response)
    # print("Got %d Hits:" % response['hits']['total']['value'])
    for hit in response['hits']['hits']:
        print(hit["_source"])
        assert hit["_source"] is not None

