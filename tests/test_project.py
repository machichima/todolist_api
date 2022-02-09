import json
from .baseCase import BaseCase

class TestCreateProject(BaseCase):
    def test_create_project(self):
        project_payload = {
            "name": "project_test",
        }
        # When
        response = self.app.post('/api/projects',
            headers={"Content-Type": "application/json"}, data=json.dumps(project_payload))

        # Then
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

class TestDeleteProject(BaseCase):
    def test_delete_project(self):
        project_payload = {
            "name": "project_test",
        }
        # When
        response = self.app.post('/api/projects',
            headers={"Content-Type": "application/json"}, data=json.dumps(project_payload))

        response_del = self.app.delete('/api/projects/' + response.json['id'])

        # Then
        self.assertEqual(200, response.status_code)

class TestUpdateProject(BaseCase):
    def test_update_project(self):
        project_payload = {
            "name": "project_test",
        }
        # When
        response = self.app.post('/api/projects',
            headers={"Content-Type": "application/json"}, data=json.dumps(project_payload))

        project_payload_put = {
            "name": "project_test_1",
        }

        response_put = self.app.put('/api/projects/' + response.json['id'], 
            headers={"Content-Type": "application/json"}, data=json.dumps(project_payload_put))

        # Then
        self.assertEqual(200, response_put.status_code)