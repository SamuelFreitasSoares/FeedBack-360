from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.init, name="home"),
=======
    path('profhome/', views.home, name="home"),
>>>>>>> 15f4e41a17e8cf4c0aee77d5e2baab0f5db24c64
    path('saida/', views.saida, name="saida"),
]