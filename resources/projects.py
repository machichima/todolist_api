from flask import Response, request
from flask_restful import Resource
from database.models import Project, User
from flask_jwt_extended import jwt_required, get_jwt_identity

class ProjectsApi(Resource):
    @jwt_required()
    def get(self):
        projects = Project.objects().to_json()
        return Response(projects, mimetype="application/json", status=200)
    
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        user = User.objects.get(id=user_id)
        body = request.get_json()
        project = Project(**body, added_by=user)
        project.save()
        user.update(push__projects=project)
        user.save()
        id = project.id
        return {'id': str(id)}, 200

class ProjectApi(Resource):
    @jwt_required()
    def get(self, id):
        project = Project.objects.get(id=id).to_json()
        return Response(project, mimetype="application/json", status=200)

    @jwt_required()
    def put(self, id):
        user_id = get_jwt_identity()
        project = Project.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        project.update(**body)
        return '', 200

    @jwt_required()
    def delete(self, id):
        user_id = get_jwt_identity()
        project = Project.objects.get(id=id, added_by=user_id)
        project.delete()
        return '', 200
