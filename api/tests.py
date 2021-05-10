from datetime import datetime

from freezegun import freeze_time

from django.test import Client
from django.test import TestCase

from .models import Student


class StudentTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @freeze_time("2020-01-01")
    def _create_student_model(self, deleted=None):
        parameter = {
            'id': 1,
            'name': 'John Doe',
            'birthdate': '2010-01-01',
            'rg': '00.000.000-0',
            'cpf': '000.000.000-00',
            'created': datetime.now(),
            'deleted': deleted,
        }
        Student.objects.create(**parameter)

    def test_list_empty_students(self):
        response = self.client.get('/api/v1/student', content_type='application/json')
        self.assertEqual(response.json()['result'], [])

    def test_get_student(self):
        self._create_student_model()

        response_data = {
            'id': 1,
            'name': 'John Doe',
            'birthdate': '2010-01-01',
            'rg': '00.000.000-0',
            'cpf': '000.000.000-00',
            'grade_id': None,
            'created': '2020-01-01',
            'deleted': None
        }
        response = self.client.get('/api/v1/student/1', content_type='application/json')
        self.assertEqual(response.json()['result'], [response_data])

    def test_create_new_student_wrong_payload(self):
        parameters = [
            {},
            {'name': 'John Doe'},
            {'name': 'John Doe', 'birthdate': '01/01/2010'},
            {'name': 'John Doe', 'birthdate': '01/01/2010', 'rg': '00.000.000-0'},
        ]
        for parameter in parameters:
            with self.subTest(parameter):
                response = self.client.post('/api/v1/student', data=parameter, content_type='application/json')

                self.assertEqual(response.json()['result'], [])
                self.assertEqual(response.status_code, 400)

    def test_create_new_student(self):
        parameter = {'name': 'John Doe', 'birthdate': '01/01/2010', 'rg': '00.000.000-0', 'cpf': '000.000.000-00'}
        response = self.client.post('/api/v1/student', data=parameter, content_type='application/json')

        self.assertEqual(response.json()['result'], {'student_id': 1})
        self.assertEqual(response.status_code, 201)

    def test_delete_nonexistent_student(self):
        response = self.client.delete('/api/v1/student/1', content_type='application/json')

        self.assertEqual(response.json()['result'], [])
        self.assertEqual(response.status_code, 404)

    def test_delete_student(self):
        self._create_student_model()

        response = self.client.delete('/api/v1/student/1', content_type='application/json')

        self.assertEqual(response.json()['result'], [])
        self.assertEqual(response.status_code, 200)

    @freeze_time("2020-01-01")
    def test_get_deleted_student(self):
        self._create_student_model(deleted=datetime.now())

        response = self.client.get('/api/v1/student/1', content_type='application/json')
        self.assertEqual(response.json()['result'], [])
