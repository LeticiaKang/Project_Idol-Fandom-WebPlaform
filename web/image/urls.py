from django.urls import path
from . import views
urlpatterns = [
    path("uploadEx", views.uploadEx_view, name='uploadEx'),
]