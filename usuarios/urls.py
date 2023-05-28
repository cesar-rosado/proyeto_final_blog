from django.contrib import admin
from django.urls import path

from usuarios.views import registro

urlpatterns = [
    path('registro/', registro, name="registro"),
]