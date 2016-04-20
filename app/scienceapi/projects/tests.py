import unittest
from django.test import Client
from . import fixtures


class ProjectTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_get_all_projects(self):
        response = self.client.get('/projects/')

        self.assertEqual(response.json(), fixtures.data)
        self.assertEqual(response.status_code, 200)
