
from api import db
import datetime

class Users(db.Model):
    __tablename__ = "users_tb"

    sequence = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=True)
    # create_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    create_date = db.Column(db.DateTime, server_default=db.func.now())
    # server_default=db.func.now(), server_onupdate=db.func.now()

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        
    # def __repr__(self):
    #     return 'UserModel(seq=%d,id=%s,name=%s,create_date=%s)' % (self.sequence, self.id, self.name, str(self.create_date))

    def json(self):
        return {'seq':self.sequence,'id': self.id, 'name': self.name, 'create_date': str(self.create_date)}
    
    
class friendships(db.Model):

    __tablename__ = "friendships"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    friend_id = db.Column(db.Integer, db.ForeignKey('users_tb.sequence', ondelete='CASCADE'))

    def json(self):
        return {'id':self.id,'id': self.id, 'name': self.name, 'friend_id': str(self.friend_id)}
