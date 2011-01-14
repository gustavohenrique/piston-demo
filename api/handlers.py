# -*- coding: utf-8 -*-
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, require_mime, require_extended

from goal.models import *

class GoalHandler(BaseHandler):
    fields = ('id', 'desc', 'latitude', 'longitude', 'achieved', 'repeat')
    model = Goal
    allowed_methods = ['GET','POST',]

    def read(self, request, pk=None):
        if pk is not None:
            return Goal.objects.filter(owner=request.user, id=pk, achieved=False)
        return Goal.objects.filter(owner=request.user, achieved=False)

    def create(self, request):
        if not request.POST: return u"Invalid data"
        try:
            data = request.POST
            params = dict(owner=request.user,desc=data['desc'],latitude=data['latitude'],longitude=data['longitude'])
            g = Goal.objects.create(**params)
            #g.save()
            return g
        except:
            pass
