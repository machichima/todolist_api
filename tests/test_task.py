import json
from .baseCase import BaseCase

class TestCreateTask(BaseCase):
    def test_create_task(self):
        # Create project
        project_payload = {
            "name": "project_test",
        }
        response_project = self.app.post('/api/projects',
            headers={"Content-Type": "application/json"}, data=json.dumps(project_payload))

        task_payload = {
            "task_name": "task_1",
            "project": str(response_project.json['id'])
        }

        response = self.app.post('/api/tasks',
            headers={"Content-Type": "application/json"}, data=json.dumps(task_payload))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

class TestDeleteTask(BaseCase):
    def test_delete_task(self):
        # Create project
        project_payload = {
            "name": "project_test",
        }
        response_project = self.app.post('/api/projects',
            headers={"Content-Type": "application/json"}, data=json.dumps(project_payload))
        
        # Create task
        task_payload = {
            "task_name": "task_1",
            "project": str(response_project.json['id'])
        }
        response_create = self.app.post('/api/tasks',
            headers={"Content-Type": "application/json"}, data=json.dumps(task_payload))

        # delete
        response = self.app.delete('/api/tasks/' + response_create.json['id'])

        self.assertEqual(200, response.status_code)

class TestUpdateTask(BaseCase):
    def test_update_task(self):
        project_payload = {
            "name": "project_test",
        }
        response_project = self.app.post('/api/projects',
            headers={"Content-Type": "application/json"}, data=json.dumps(project_payload))
        
        # Create task
        task_payload = {
            "task_name": "task_1",
            "project": str(response_project.json['id'])
        }
        response_create = self.app.post('/api/tasks',
            headers={"Content-Type": "application/json"}, data=json.dumps(task_payload))

        # put
        task_payload_put = {
            "task_name": "task_1_put",
        }
        response = self.app.put('/api/tasks/' + response_create.json['id'], 
            headers={"Content-Type": "application/json"}, data=json.dumps(task_payload_put))

        self.assertEqual(200, response.status_code)

class TestGetTasksofSameProject(BaseCase):
    def test_get_task_of_same_project(self):
        project_payload = {
            "name": "project_test",
        }
        response_project = self.app.post('/api/projects',
            headers={"Content-Type": "application/json"}, data=json.dumps(project_payload))
        
        # Create task
        task_payload_1 = {
            "task_name": "task_1",
            "project": str(response_project.json['id'])
        }
        task_payload_2 = {
            "task_name": "task_2",
            "project": str(response_project.json['id'])
        }
        self.app.post('/api/tasks',
            headers={"Content-Type": "application/json"}, data=json.dumps(task_payload_1))
        self.app.post('/api/tasks',
            headers={"Content-Type": "application/json"}, data=json.dumps(task_payload_2))

        response = self.app.get('/api/projects/' + response_project.json['id'] + '/tasks')

        self.assertEqual("task_1", response.json[0]['task_name'])
        self.assertEqual("task_2", response.json[1]['task_name'])
        self.assertEqual(200, response.status_code)