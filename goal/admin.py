# -*- coding: utf-8 -*-
from django.contrib.admin import site, ModelAdmin
from goal.models import *

class GoalAdmin(ModelAdmin):
    list_display = ('desc', 'owner', 'latitude', 'longitude', 'achieved', 'repeat')
    list_filter = ('owner', 'achieved', 'repeat')
    ordering = ('-id',)
site.register(Goal, GoalAdmin)
