import json

import connexion
from api import logger

from api.repository.repo import (UserRepo)
from api.repository.schema import (UserSchema)


userRepo = UserRepo()
userSchema = UserSchema()


def api_get():
    try:
        # query_req_json = request.get_json()
        # results = SearchOmniHandlerObject.search(query_builder=QueryBuilderObject, oas_query=query_req_json)
        results = userRepo.fetchAll()
        logger.info("api_get..")
        return results, 200
    except Exception as ex:
        return ex, 500