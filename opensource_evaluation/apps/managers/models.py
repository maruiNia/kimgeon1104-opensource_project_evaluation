from django.db import models

# Create your models here.

class Projects(models.Model) :
    project_name = models.CharField(max_length=100, primary_key=True)
    project_explain_image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.project_name
    
class Projects_star(models.Model) :
    project_name = models.ForeignKey(Projects, on_delete=models.CASCADE)
    projects_star = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.project_name} : {Projects_star}"