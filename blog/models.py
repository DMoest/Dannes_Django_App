#!/usr/bin/env python3

from django.db.models import (
    Model,
    CharField,
    TextField,
)


# Create your models here.
class Blog(Model):
    title = CharField(max_length=55)
    content = TextField()
