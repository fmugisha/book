from django.urls import path
from . import views

urlpatterns = [
    path('', views.borrowed, name="borrowed")
]