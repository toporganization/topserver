from __future__ import unicode_literals

from django.db import models

# Create your models here.
class New(models.Model):
    title = models.TextField()
    content = models.TextField()
