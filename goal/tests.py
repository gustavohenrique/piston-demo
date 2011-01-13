"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from goal.models import *

def factory(**kwargs):
    params = dict(desc='Buy milk', latitude='-19.999208', longitude='-43.967591', achieved=False, repeat=False)
    params.update(**kwargs)
    return Goal(**params)


class TestModels(TestCase):

    fixtures = ['auth.json', 'goal.json']

    def setUp(self):
        self.user = User.objects.get(username='admin')

    def test_create_goal(self):
        goal = factory(owner=self.user)
        goal.save()
        self.assertEquals(3, goal.id)

    def test_find_not_achieved_by_user(self):
        goals = Goal.objects.filter(owner=self.user, achieved=False)
        self.assertEquals(1, goals.count())


from django.test.client import Client

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
