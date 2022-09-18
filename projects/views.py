#!/usr/bin/env python3

from django.shortcuts import render

from projects.models import Project


def all_projects(request):
    """
    It takes a request, gets all the projects, and renders a template with the projects

    :param request: This is the request object that is sent to the view
    :return: A list of all projects
    """
    projects = Project.objects.all()

    return render(
        request,
        'projects/all_projects.html',
        {
            'projects': projects
        }
    )


def project_detail(request, pk):
    """
    It takes a request and a primary key, gets the project with that primary key, and renders a template with the project

    :param request: The request object is the first parameter to every view. It contains information about the request that
    was made to the server
    :param pk: The primary key of the project we want to display
    :type pk: int
    :return: The project_detail view is returning a render of the project_detail.html template.
    """
    project = Project.objects.get(pk=pk)

    return render(
        request,
        'projects/detail.html',
        {
            'project': project
        }
    )
