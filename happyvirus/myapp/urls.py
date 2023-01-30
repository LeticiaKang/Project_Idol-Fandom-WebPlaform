from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('join', views.register, name='join'),
    path('login', views.login, name='login'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
]


