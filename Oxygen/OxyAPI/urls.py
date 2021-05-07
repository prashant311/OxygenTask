from django.contrib import admin
from django.urls import path
from .views import oxy_create, oxy_list

urlpatterns = [
    path('oxy_list', oxy_list, name="oxygen-list"),
    path('oxy_create', oxy_create, name="oxygen-create"),
]
