# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication, HttpBasicSimple
from api.handlers import *

auth = HttpBasicAuthentication(realm='Goal')
goal_resource = Resource(handler=GoalHandler, authentication=auth)

urlpatterns = patterns('',
    (r'^goals/$', goal_resource),
    (r'^goals/(?P<pk>[^/]+)', goal_resource),
    #(r'^goals/(?P<sigla_estado>[^/]+)', cidade_resource),
    (r'^add/$', goal_resource),
)
