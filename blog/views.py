#!/usr/bin/env python3

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

from blog.models import Blog


# Create your views here.
def blog_listing(request):
    """
    It takes a request, and returns a response

    :param request: This is the request object that is sent to the view. It contains all the information about the request,
    including the HTTP method, the URL, the headers, the body, and so on
    :type request: HttpRequest

    :return: The data is being returned.
    :rtype: HttpResponse
    """
    data = {
        'blogs': Blog.objects.all()
    }

    return render(request, 'listing.html', data)


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    data = {'blog': blog}

    return render(request, 'detail.html', data)


def see_request(request):
    text = f"""
    Some attributes of the request object:
    scheme: {request.scheme}
    path: {request.path}
    method: {request.method}
    GET: {request.GET}
    user: {request.user}
    """

    return HttpResponse(text, content_type='text/plain')


def user_info(request):
    text = f"""
    Some user attributes of the request object:
    username: {request.user.username}
    is_anonymous: {request.user.is_anonymous}
    is_authenticated: {request.user.is_authenticated}
    is_staff: {request.user.is_staff}
    is_superuser: {request.user.is_superuser}
    is_active: {request.user.is_active}
    """

    return HttpResponse(text, content_type='text/plain')


@login_required
def privet_place(request):
    return HttpResponse('This is a private place', content_type='text/plain')


@user_passes_test(lambda user: user.is_staff)
def staff_place(request):
    return HttpResponse('User is staff!', content_type='text/plain')


@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f'Hello {username}')
    messages.add_message(request, messages.WARNING, f'DANGER will get you {username}!')

    return HttpResponse('Messages Added', content_type='text/plain')