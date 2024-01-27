
from api import *
from .model import (Users)
from typing import List
import json

class UserRepo:
    '''
    https://velog.io/@sugenius77/SQLAlchemy-ORM
    '''

    def create(self, item):
        logger.info('create -> {}'.format(item))
        db.session.add(item)
        db.session.commit()

    def fetchById(self, _id) -> 'Item':
        itemRepo =  db.session.query(Item).filter(Item.id == _id).first()
        if itemRepo:
            logger.info('fetchById -> {}'.format(json.dumps(itemRepo.json(), indent=2)))
        return itemRepo
        # return db.session.query(Item).filter_by(id=_id).first()

    def fetchAll(self) -> List['Item']:
        itemRepo = db.session.query(Item).all()
        itemRepos = [obj.json() for obj in itemRepo]
        logger.info('fetchAll -> {}'.format(json.dumps(itemRepos, indent=2)))
        return itemRepo
    
    def fetch_Page_All(self, page, page_size) -> List['Item']:
        skip = (page_size - 1) * page
        logger.info('fetch_Page_All Parameters -> page : {}, pageSize : {}'.format(page, page_size))
        # print('fetchAll -> ', db.session.query(Item).limit(page_size).offset(page*page_size).all())
        # return db.session.query(Item).all()
        itemRepo = db.session.query(Item).limit(page).offset(skip).all()
        itemRepos = [obj.json() for obj in itemRepo]
        logger.info('fetch_Page_All -> {}'.format(json.dumps(itemRepos, indent=2)))
        return itemRepo
        
    def delete(self, _id) -> None:
        logger.info('delete: {}'.format(_id))
        item = db.session.query(Item).filter_by(id=_id).first()
        db.session.delete(item)
        db.session.commit()

    def update(self, item_data):
        print('update -> ', item_data)
        db.session.merge(item_data)
        db.session.commit()