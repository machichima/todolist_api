from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Project(db.Document):
    name = db.StringField(required=True, unique=True)
    tasks = db.ListField(db.ReferenceField('Task'), reverse_delete_rule=db.PULL)
    added_by = db.ReferenceField('User')
    

class Task(db.Document):
    task_name = db.StringField(required=True, unique=True)
    is_done = db.BooleanField(default=False)
    project = db.ReferenceField('Project', required=True)

Project.register_delete_rule(Task, 'project', db.CASCADE)

class User(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    projects = db.ListField(db.ReferenceField('Project'), reverse_delete_rule=db.PULL)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Project, 'added_by', db.CASCADE)   # 不確定，查一下