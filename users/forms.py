#!/usr/bin/env python3

"""
Custom user registration form including email field.
"""

from django.contrib.auth.forms import UserCreationForm


class CustomUserRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)
