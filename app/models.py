from app import db

import datetime

class Todo(db.Document):
    content = db.StringField(max_length=30, required=True)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)