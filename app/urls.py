from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('start', views.index, name='index'),
    path('', views.start, name='start'),

]
