from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("main", views.main, name='main'),
    path('join', views.register, name='join'),
    path('login', views.login, name='login'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('mypage', views.mypage, name='mypage'),
    path('upload', views.upload, name='upload'),
    path('collection', views.collection, name='collection'),
    path('upload_list', views.upload_list, name='upload_list'),
]


