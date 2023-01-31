from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('join', views.register, name='join'),
    path('login', views.login, name='login'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('mypage', views.mypage, name='mypage'),
    path('upload', views.upload, name='upload'),
    path('result', views.result, name='result'),
    path('collection', views.collection, name='collection'),
    path('upload_list', views.upload_list, name='upload_list'),

   
]


