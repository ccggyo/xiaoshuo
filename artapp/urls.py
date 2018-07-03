from django.contrib import admin
from django.urls import path

from artapp import views

urlpatterns = [
    path('', views.index),
]
