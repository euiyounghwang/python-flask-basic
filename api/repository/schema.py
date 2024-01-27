# from ma import ma
from api import ma

from .model import Users


class UserSchema(ma.SQLAlchemyAutoSchema):
# class ItemSchema():
    class Meta:
        model = Users
        load_instance = True