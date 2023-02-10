from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),

    path('join', views.register, name='join'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('mypage', views.modify_view, name='mypage'),
    path('change_pw', views.change_pw_view, name='change_pw'),
    path('delete', views.delete_view,  name='delete'),
    

    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact'),
    path('mypage', views.mypage, name='mypage'),
    path('upload', views.upload, name='upload'),
    path('collection', views.collection, name='collection'),
    path('upload_list', views.upload_list, name='upload_list'),

    
    
    
    path('posting_list', views.posting_list, name='posting_list'),
    path('<int:posting_id>/', views.posting_detail, name='posting_detail'),
    path('create/', views.create_posting, name='create_posting'),
    path('<int:posting_id>/delete/', views.delete_posting, name='delete_posting'),
    path('<int:posting_id>/comments/create', views.create_comment, name='create_comment'),
    path('<int:posting_id>/comments/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),

    path('feed', views.feed, name='feed'),


]