import pytest
#from django.contrib.auth.models import User
from django.test import TestCase
from model_mommy import mommy
from .models import Post

class PostTestModel(TestCase):
   def setUp(self):
       self.User = mommy.make(User)
       self.post = Post(user=self.user)
#        
#    def test_publish(self):
#        
