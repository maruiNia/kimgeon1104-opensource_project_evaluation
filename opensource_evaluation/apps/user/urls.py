from django.urls import path
from . import views

app_name = "user"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('project/<str:project_name>/',views.project_detail, name="project_detail"),
    path('project/<str:project_name>/result/',views.project_result, name="project_result"),
]