from .projects import ProjectApi, ProjectsApi
from .tasks import TaskApi, TasksApi, TasksForProjectApi

def init_route(api):
    app.add_resource(ProjectsApi, '/api/projects')
    app.add_resource(ProjectApi, '/api/projects/<id>')

    app.add_resource(TasksForProjectApi, '/api/projects/<project_id>/tasks')
    app.add_resource(TasksApi, '/api/tasks')
    app.add_resource(TaskApi, '/api/tasks/<task_id>')