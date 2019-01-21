# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Invite_Form(models.Model):
	name = models.CharField(max_length=150)
	invitation_msg = models.CharField(max_length=50)
	datetime = models.DateTimeField()
	venue_name = models.CharField(max_length=50)
	detail_venue = models.CharField(max_length=50)
