
from api import *
from .model import (Users, friendships)
from typing import List
import json

class UserRepo:
    '''
    https://velog.io/@sugenius77/SQLAlchemy-ORM
    '''

    def create(self, users):
        # logger.info('create -> {}, id : {}'.format(users, users.id))
        # logger.info(type(users))
        logger.info('create -> {}, id : {}'.format(users, users.get("id")))
        # if not self.fetchById(users.id):
        if not self.fetchById(users.get("id")):
            users_init = Users(id=users.get("id"), name=users.get("name"), email=users.get('email',''))
            # db.session.add(users)
            db.session.add(users_init)
            db.session.commit()
            return users
        return None

    def fetchById(self, _id) -> Users:
        logger.info('Repo fetchById')
        # userRepo =  db.session.query(Users).filter(Users.id == _id).first()
        userRepo =  db.session.query(Users).filter_by(id=_id).first()
        if userRepo:
            logger.info('fetchById (Exist) -> {}'.format(json.dumps(userRepo.json(), indent=2)))
        return userRepo
        

    def fetchAll(self) -> List['Users']:
        # userRepo = db.session.query(Users).all()
        # .filter(Users.sequence == friendships.friend_id) \
        userRepo = db.session.query(Users, friendships) \
                    .filter(Users.sequence == friendships.friend_id) \
                    .add_columns(Users.sequence, Users.id, Users.name, Users.email, friendships.id.label("f_id")).all()
        
        print(userRepo, type(userRepo))       
        """ 
        userRepos = [obj.json() for obj in userRepo]
        if userRepos:
            logger.info('fetchAll -> {}'.format(json.dumps(userRepos, indent=2)))
        """
        userRepos = [
                {
                    "sequence" : obj.sequence,
                    "id" : obj.id,
                    "name" : obj.name,
                    "email" : obj.email,
                    "friendships" : {
                        "id" : obj.f_id
                    }
                }   
                for obj in userRepo
            ]
        if userRepos:
            logger.info("{}".format(json.dumps(userRepos, indent=2)))
            return userRepos
        return None
    
    def fetch_Page_All(self, page, page_size) -> List['Users']:
        skip = (page_size - 1) * page
        logger.info('fetch_Page_All Parameters -> page : {}, pageSize : {}'.format(page, page_size))
        # print('fetchAll -> ', db.session.query(Item).limit(page_size).offset(page*page_size).all())
        # return db.session.query(Item).all()
        userRepo = db.session.query(Users).limit(page).offset(skip).all()
        userRepos = [obj.json() for obj in userRepo]
        logger.info('fetch_Page_All -> {}'.format(json.dumps(userRepos, indent=2)))
        return userRepos
        
    def delete(self, _id) -> Users:
        logger.info('delete: {}'.format(_id))
        user = db.session.query(Users).filter_by(id=_id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return user
        return None

    def update(self, item_data):
        print('update -> ', item_data)
        db.session.merge(item_data)
        db.session.commit()