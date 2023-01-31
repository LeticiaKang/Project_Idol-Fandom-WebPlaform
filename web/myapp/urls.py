from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),

    path('join', views.register, name='join'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('mypage', views.mypage, name='mypage'),
    path('upload', views.upload, name='upload'),
    path('collection', views.collection, name='collection'),
    path('upload_list', views.upload_list, name='upload_list'),

]