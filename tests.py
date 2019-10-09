from django.test import TestCase


# Webserver run하면 200이 안 떨어지는지 확인
class WebServerRunTests(TestCase):
    def test_is_run(self):
        response = self.client.get('127.0.0.1:8000')
        self.assertEqual(response.status_code, 404)
        self.assertNotEqual(response.status_code, 200)
