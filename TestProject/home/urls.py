from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name='home'),
    path('join', views.register, name='join'),
    path('login', views.login, name='login'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
]