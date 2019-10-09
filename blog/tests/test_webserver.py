import pytest

from django.test import TestCase

class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x


# class WebServerRunTests(TestCase):
#     def test_is_run(self):
#         response = self.client.get('127.0.0.1:8000')
#         self.assertEqual(response.status_code, 404)
#         self.assertNotEqual(response.status_code, 200)