from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProjectsModelForm
from .models import Projects

# Create your views here.

from django.http import HttpResponse

def index(request) :
    all_projects_list = Projects.objects.order_by('project_name')
    context = {'all_projects_list' : all_projects_list}
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
        