#!/usr/bin/env python3

"""
Django ORM models for projects app.
"""
from django.db.models import (CharField, Model, TextField)


# Create your models here.
class Project(Model):
    title = CharField(max_length=100, blank=False, null=False, default="")
    description = TextField(blank=False, null=False, default="")
    short_description = CharField(max_length=255, blank=False, null=False, default="")
    technology = CharField(max_length=20, blank=True, null=False, default="Django")
    link = CharField(max_length=255, blank=True, null=False, default="")
    colaborators = CharField(max_length=255, blank=True, null=False, default="")
    image = CharField(max_length=255, blank=True, null=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ('id', 'title', 'technology')
