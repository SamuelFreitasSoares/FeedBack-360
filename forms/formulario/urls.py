from django.urls import path
from . import views

urlpatterns = [
    path('entrada/', views.home, name="home"),
    path('saida/', views.saida, name="saida"),
]