from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name='home'),
    path('join', views.register, name='join')
]