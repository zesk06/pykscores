#!/usr/bin/env python3
# encoding: utf-8

from mongoengine import *

connect(db='zesk06_test', host='ds061206.mlab.com', port=61206,
        username='zesk06', password='1Ado6Tic3Tank_m')


class User(Document):
    email = StringField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)


ross = User(email='toto@gmail.com', first_name='toto', last_name='doe')
ross.save()
print(f'{ross.email} has been saved')
