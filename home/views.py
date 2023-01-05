from django.shortcuts import render
from books.models import Book

# Create your views here.
def home(request):

    book = Book.objects.all().values()

    books = {
        'books':book
    }

    return render(request, 'home.html', books)