from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project(models.Model):
    id_proj = models.IntegerField(unique=True, primary_key=True)