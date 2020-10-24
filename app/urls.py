from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entries', views.entries, name='entries'),
]