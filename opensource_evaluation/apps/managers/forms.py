from django import forms
from .models import Projects

class ProjectsModelForm(forms.ModelForm) :
    class Meta:
        model = Projects
        fields = ['project_name', 'project_explain_image']