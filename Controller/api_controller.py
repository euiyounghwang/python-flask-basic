import json

import connexion
from main import logger


def api_get():
    try:
        # query_req_json = request.get_json()
        # results = SearchOmniHandlerObject.search(query_builder=QueryBuilderObject, oas_query=query_req_json)
        return {}, 200
    except Exception as ex:
        return ex, 500