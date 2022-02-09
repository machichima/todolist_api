from asyncio import tasks
from flask import Response, request
from flask_restful import Resource
from database.models import Task
from flask_jwt_extended import jwt_required, get_jwt_identity

class TasksForProjectApi(Resource):
    @jwt_required()
    def get(self, project_id):
        tasks = Task.objects.filter(project=project_id).to_json()
        return Response(tasks, mimetype="application/json", status=200)

class TasksApi(Resource):
    @jwt_required()
    def post(self):
        body = request.get_json()
        task = Task(**body)
        task.save()
        id = task.id
        return {'id': str(id)}, 200

class TaskApi(Resource):
    @jwt_required()
    def get(self, task_id):
        task = Task.objects.get(id=task_id).to_json()
        return Response(task, mimetype="application/json", status=200)

    @jwt_required()
    def put(self, task_id):
        body = request.get_json()
        task = Task.objects.get(id=task_id)
        task.update(**body)
        return '', 200

    @jwt_required()
    def delete(self, task_id):
        task = Task.objects.get(id=task_id)
        task.delete()
        return '', 200
    
    