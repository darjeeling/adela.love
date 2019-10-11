import pytest

from django.test import TestCase

# unittest에서는 잘 돌아갔던 코드인데 pytest에서는 어떻게 돌리는게 좋을까?
# class WebServerRunTests(TestCase):
#     def test_is_run(self):
#         response = self.client.get('127.0.0.1:8000')
#         self.assertEqual(response.status_code, 404)
#         self.assertNotEqual(response.status_code, 200)

# 아무런 설정 없이 시험 삼아 돌렸을 때 pytest에서 잘 돌아갔던 코드  
class TestClass:
    def test_one(self):
        x = 'this'
        assert 'h' in x

