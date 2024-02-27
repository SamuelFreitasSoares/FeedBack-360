from django.urls import path
from . import views

urlpatterns = [
    path('', views.init, name="home"),
    path('saida/', views.saida, name="saida"),
]