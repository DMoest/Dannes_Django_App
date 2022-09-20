#!/usr/bin/env python3

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Blog


# Create your views here.
def listing(request):
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
