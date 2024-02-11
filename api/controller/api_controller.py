import json

import connexion
from api import logger, db
from flask import request
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
    
    
    
def omni_db_entity_create_json():
    try:
        user_req_json = request.get_json()
        logger.info("omni_db_entity_create_json -> {}".format(user_req_json))
        
        # user_data = userSchema.load(user_req_json, session=db.session)
        # response = userRepo.create(user_data)
        response = userRepo.create(user_req_json)
        if response:
            # return userSchema.dump(user_data),201
            return user_req_json,201
        return {'message': 'ITEM_EXIST'}, 404
    except Exception as ex:
        logger.error(ex)
        return {"message" : ex}, 500

   
    
def omni_db_entity_fetchbyid_json(_id):
    try:
        results = userRepo.fetchById(_id)
        if results:
            return results.json(), 200
        return {'message': ITEM_NOT_FOUND.format(_id)}, 404
        
    except Exception as ex:
        logger.error(ex)
        return ex, 500
    
    
def omni_db_entity_delete_json(_id):
    try:
        results = userRepo.delete(_id)
        if results:
            return results.json(), 200
        return {'message': ITEM_NOT_FOUND.format(_id)}, 404
        
    except Exception as ex:
        logger.error(ex)
        return ex, 500