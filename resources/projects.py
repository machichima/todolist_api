from flask import Response, request
from flask_restful import Resource
from database.models import Project

class ProjectsApi(Resource):
    def get(self):
        projects = Project.objects().to_json()
        return Response(projects, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        project = Project(**body)
        project.save()
        id = project.id
        return {'id': str(id)}, 200

class ProjectApi(Resource):
    def get(self, id):
        project = Project.objects.get(id=id).to_json()
        return Response(project, mimetype="application/json", status=200)

    def put(self, id):
        project = Project.objects.get(id=id)
        body = request.get_json()
        project.update(**body)
        return '', 200

    def delete(self, id):
        project = Project.objects.get(id=id)
        project.delete()
        return '', 200
