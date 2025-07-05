from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from apps.managers.models import Projects, Projects_star
from django.urls import reverse
from django.db import models

# Create your views here.

def index(request) :
    projects_list = Projects.objects.values("project_name")
    list = []
    for project in projects_list :
        list.append(project['project_name'])

    context = {"list" : list}

    return render(request, "user/index.html", context)

def project_detail(request, project_name) :
    project = get_object_or_404(Projects, pk=project_name)

    if request.method == 'POST' :
        starpoint = int(request.POST.get('starpoint'))

        Projects_star.objects.create(
            project_name = project,
            projects_starpoint = starpoint
        )

        return redirect(reverse("user:project_result", args=[project.project_name]))
    
    context = {
        'project' : project
    }

    return render(request, 'user/project_detail.html', context)

def project_result(request, project_name) :
    project = get_object_or_404(Projects, pk=project_name)

    stars = Projects_star.objects.filter(project_name=project)

    count = stars.count()
    avg = stars.aggregate(models.Avg('projects_starpoint'))['projects_starpoint__avg'] or 0

    context = {
        'project' : project,
        'count' : count,
        'avg' : round(avg,2),
    }
    return render(request, 'user/project_result.html', context)

    