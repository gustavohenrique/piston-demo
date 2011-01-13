# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    owner = models.ForeignKey(User)
    desc = models.CharField('Description', max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    achieved = models.BooleanField(default=False)
    repeat = models.BooleanField(default=False)

    def __unicode__(self):
        return self.desc
