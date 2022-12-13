from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin, name="admin"),
    path('books/', views.books, name="books"),
    path('users/', views.users, name="users"),
    path('change/', views.change, name="change")
]