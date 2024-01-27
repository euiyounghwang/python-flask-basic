
from api import *
from .model import (Users)
from typing import List
import json

class UserRepo:
    '''
    https://velog.io/@sugenius77/SQLAlchemy-ORM
    '''

    def create(self, users):
        logger.info('create -> {}'.format(users))
        db.session.add(users)
        db.session.commit()

    def fetchById(self, _id) -> 'Users':
        userRepo =  db.session.query(Users).filter(Item.id == _id).first()
        if userRepo:
            logger.info('fetchById -> {}'.format(json.dumps(userRepo.json(), indent=2)))
        return userRepo
        # return db.session.query(Item).filter_by(id=_id).first()

    def fetchAll(self) -> List['Users']:
        userRepo = db.session.query(Users).all()
        userRepos = [obj.json() for obj in userRepo]
        logger.info('fetchAll -> {}'.format(json.dumps(userRepos, indent=2)))
        return userRepos
    
    def fetch_Page_All(self, page, page_size) -> List['Users']:
        skip = (page_size - 1) * page
        logger.info('fetch_Page_All Parameters -> page : {}, pageSize : {}'.format(page, page_size))
        # print('fetchAll -> ', db.session.query(Item).limit(page_size).offset(page*page_size).all())
        # return db.session.query(Item).all()
        userRepo = db.session.query(Users).limit(page).offset(skip).all()
        userRepos = [obj.json() for obj in userRepo]
        logger.info('fetch_Page_All -> {}'.format(json.dumps(userRepos, indent=2)))
        return userRepos
        
    def delete(self, _id) -> None:
        logger.info('delete: {}'.format(_id))
        user = db.session.query(Users).filter_by(id=_id).first()
        db.session.delete(user)
        db.session.commit()

    def update(self, item_data):
        print('update -> ', item_data)
        db.session.merge(item_data)
        db.session.commit()