from django.db import models

# Create your models here.

class Projects(models.Model) :
    project_name = models.CharField(max_length=100)
    project_explain_image = models.ImageField(upload_to='image/')
    project_total_star = models.IntegerField()