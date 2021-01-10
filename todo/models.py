# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title