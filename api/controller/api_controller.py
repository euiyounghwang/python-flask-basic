import json

import connexion
from api import logger

from api.repository.repo import (UserRepo)
from api.repository.schema import (UserSchema)


userRepo = UserRepo()
userSchema = UserSchema()

ITEM_NOT_FOUND = "Item not found for id: {}"

def omni_db_entity_all_json():
    try:
        results = userRepo.fetchAll()
        if results:
            return results, 200
        return {'message': 'ITEM_NOT_FOUND'}, 404
    except Exception as ex:
        logger.error(ex)
        return ex, 500
    
    
def omni_db_entity_fetchbyid_json(_id):
    try:
        results = userRepo.fetchById(_id)
        if results:
            return results.json(), 200
        return {'message': ITEM_NOT_FOUND.format(_id)}, 404
        
    except Exception as ex:
        logger.error(ex)
        return ex, 500