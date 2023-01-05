from django.urls import path
from . import views

urlpatterns = [
    path('', views.books, name="books"),
    path('book_store', views.book_store, name="book_store"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit"),
    path('edit/editrecord/<int:id>', views.editrecord, name="editrecord"),
]