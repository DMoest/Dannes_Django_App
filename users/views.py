#!/usr/bin/env python3

"""
Routes for Users app.
"""

from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import CustomUserRegisterForm


def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    if request.method == 'GET':
        return render(
            request,
            'users/register.html',
            {'form': CustomUserRegisterForm}
        )
    elif request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            new_user.save()
            login(request, new_user)

            return redirect(reverse('dashboard'))


def password_reset_complete(request):
    return render(request, 'users/registration/password_reset_complete.html')
