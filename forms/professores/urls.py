from django.urls import path
from . import views

urlpatterns = [
    path('profhome/', views.home, name="home"),
    path('saida/', views.saida, name="saida"),
]