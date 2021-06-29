#https://djangobook.com/mdj2-models/

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from django.core.management import call_command

from django.db import models

class Event(models.Model):
        name = models.CharField('Event Name', max_length=120)
        event_date = models.DateTimeField('Event Date')
        venue = models.CharField(max_length=120)
        manager = models.CharField(max_length=60)
        description = models.TextField(blank=True)
        
