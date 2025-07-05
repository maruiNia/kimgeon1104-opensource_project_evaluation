from django.urls import path
from . import views

app_name = 'managers'
urlpatterns = [
    path('index/', views.index, name="index"),  #리스트 보여주기 및 추가하는 방법
    path('upload_view/', views.upload_view, name="upload_view"), # 추가
    # path('upload/', views.upload_view, name="upload_view"),
]