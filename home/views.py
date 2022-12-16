from django.shortcuts import render
from books.models import Books

# Create your views here.
def home(request):

    book = Books.objects.all()

    books = {
        'books':book
    }

    return render(request, 'home.html', books)