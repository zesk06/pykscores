# pylint fail to discover some mongoengin members
# pylint: disable=E1101
import logging

from mongoengine import connect as me_connect
from mongoengine import Document, StringField, IntField
from mongoengine import DateTimeField
from mongoengine import EmbeddedDocumentListField
from mongoengine import EmbeddedDocument
from mongoengine import ReferenceField


def connect(host='', port=0, password=''):
    # me_connect(db='zesk06_test',
    #            host='XXXXXXX.mlab.com',
    #            port=XXXXXX,
    #            username='zesk06', password='MUHAHA')
    me_connect(db='pykscores_test')


class User(Document):
    email = StringField()
    login = StringField(required=True)
    first_name = StringField()
    last_name = StringField()

    @staticmethod
    def find_one(login, create=False):
        users = User.objects(login=login)
        if users:
            return users[0]
        if create:
            new_user = User(login=login)
            new_user.save()
            logging.debug(f'Autocreated {new_user}')
            return new_user
        raise KeyError(f'login not found {login}')

    def __repr__(self):
        return f'User(login="{self.login}")'


class UserScore(EmbeddedDocument):
    user = ReferenceField(User)
    score = IntField(required=True)
    color = StringField()
    team = StringField()
    team_color = StringField()

    def __repr__(self):
        return f'UserScore(login="{self.user.login}", score={self.score})'


class Play(Document):
    date = DateTimeField(required=True)
    scores = EmbeddedDocumentListField(UserScore)

    def __repr__(self):
        return f'Play(data="{self.date}", scores={self.scores})'
