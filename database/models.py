from .db import db

class Project(db.Document):
    name = db.StringField(required=True, unique=True)
    tasks = db.ListField(db.ReferenceField('Task'))
    

class Task(db.Document):
    task_name = db.StringField(required=True, unique=True)
    is_done = db.BooleanField(default=False)
    project = db.ReferenceField('Project', reverse_delete_rule=db.PULL)