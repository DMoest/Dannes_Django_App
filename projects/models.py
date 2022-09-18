#!/usr/bin/env python3

"""
Django ORM models for projects app.
"""
from django.db.models import (CharField, Model, TextField)


# Create your models here.
class Project(Model):
    title = CharField(max_length=100)
    description = TextField()
    technology = CharField(max_length=20)
    image = CharField(max_length=100)
