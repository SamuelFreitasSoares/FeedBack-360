from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name="upload_file"),
    path('saida/', views.saida, name="saida"),
    path('upload/', views.upload_file, name="upload_file"),
]