import json

import connexion
from api import logger

from api.repository.transaction import (UserRepo)
from api.repository.schema import (UserSchema)


userRepo = UserRepo()
userSchema = UserSchema()

def index():
    logger.info("call..")
    return render_template('index.html')


def api_get():
    try:
        # query_req_json = request.get_json()
        # results = SearchOmniHandlerObject.search(query_builder=QueryBuilderObject, oas_query=query_req_json)
        logger.info("call..")
        return {}, 200
    except Exception as ex:
        return ex, 500