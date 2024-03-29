#!/usr/bin/env python3

"""
Users module routes.
"""

from django.urls import include, path

from users.views import dashboard, register

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
]
