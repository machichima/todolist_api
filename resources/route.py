from .projects import ProjectApi, ProjectsApi
from .tasks import TaskApi, TasksForProjectApi
from .auth import SignUpApi, LogInApi

def init_route(api):
    api.add_resource(ProjectsApi, '/api/projects')
    api.add_resource(ProjectApi, '/api/projects/<id>')

    api.add_resource(TasksForProjectApi, '/api/projects/<project_id>/tasks')
    #api.add_resource(TasksApi, '/api/tasks')
    api.add_resource(TaskApi, '/api/tasks/<task_id>')

    api.add_resource(SignUpApi, '/api/auth/signup')
    api.add_resource(LogInApi, '/api/auth/login')