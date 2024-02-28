from django.urls import path
from . import views
urlpatterns = [
    path("upload", views.upload_view, name='upload'),
    path("upload_list", views.upload_list, name='upload_list'),
]