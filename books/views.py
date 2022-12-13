from django.shortcuts import render
from book_site.models import User

def books(request):
    return render(request, 'book.html')