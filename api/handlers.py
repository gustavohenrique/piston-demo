# -*- coding: utf-8 -*-
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from goal.models import *

class GoalHandler(BaseHandler):
    model = Goal
    allowed_methods = ('GET',)

    def read(self, request):
        return Goal.objects.filter(owner=request.user, achieved=False)

    #def create(self, request):
    #    if request.content_type and request.data:
    #        data = request.data
    #        params = dict(owner=request.user, 
