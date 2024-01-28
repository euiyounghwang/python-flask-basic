
from api import db
import datetime

class Users(db.Model):
    __tablename__ = "users_tb"

    sequence = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(20), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False)
    # create_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    create_date = db.Column(db.DateTime, server_default=db.func.now())
    # server_default=db.func.now(), server_onupdate=db.func.now()

    # def __repr__(self):
    #     return 'UserModel(seq=%d,id=%s,name=%s,create_date=%s)' % (self.sequence, self.id, self.name, str(self.create_date))

    def json(self):
        return {'seq':self.sequence,'id': self.id, 'name': self.name, 'create_date': str(self.create_date)}