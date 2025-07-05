from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProjectsModelForm
from django.db import connection
from django.db.models import Model

from .models import Projects
from django.db.models import Avg
from django.http import HttpResponse

# Create your views here.

def index(request) :
    # all_projects_list = Projects.objects.order_by('project_name')
    # context = {'all_projects_list' : all_projects_list}

    all_projects_list = Projects.objects.annotate(
        avg_star = Avg('projects_star__projects_starpoint')
    ).order_by('-avg_star')

    context = {"all_projects_list" : all_projects_list}

    return render(request, 'managers/projectList.html', context)

def upload_view(request) :
    if request.method == 'POST' :
        
        #파일 포함
        form = ProjectsModelForm(request.POST, request.FILES)

        if form.is_valid() :
            form.save()
            return redirect(reverse('managers:index'))
        
    else :
        form = ProjectsModelForm()
    
    return render(request, 'managers/upload.html', {"form" : form})
    # return HttpResponse("i'm upload")
        