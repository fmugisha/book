from django.shortcuts import render, redirect
from books.models import Books
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

def books(request):

    book = Books.objects.all().order_by('id')

    books = {
        'books':book
    }

    return render(request, 'book.html', books)

def book_store(request):
    if request.method == "POST":
        bookName = request.POST['bname']
        bookAuthor = request.POST['bauthor']
        bookDescription = request.POST['bdesc']
        bookNumbers = request.POST['bnum']
        bookImage = request.POST['bimg']

        if Books.objects.filter(bookName=bookName).exists():
            messages.info(request, 'This book is already exist!')
            return redirect('/')
        else:
            book = Books(bookName=bookName, bookAuthor=bookAuthor, bookDescription=bookDescription, bookTotal=bookNumbers, bookImage=bookImage)
            book.save();
            return redirect('books')
    else:
        return redirect('books')

def delete(request, id):

    delBook = Books.objects.get(id=id)
    delBook.delete()

    return redirect('books')

def edit(request, id):
  editbook = Books.objects.get(id=id)
  book = Books.objects.all().order_by('id')
  template = loader.get_template('bookedit.html')
  context = {
    'bookedit': editbook,
    'books': book,
  }
  return HttpResponse(template.render(context, request))

def editrecord(request, id):
    name = request.POST['ename']
    author = request.POST['eauthor']
    description = request.POST['edesc']
    total = request.POST['enumber']
    image = request.POST['eimage']

    edited = Books.objects.get(id=id)
    edited.bookName = name
    edited.bookAuthor = author
    edited.bookDescription = description
    edited.bookTotal = total
    edited.bookImage = image
    edited.save()

    return HttpResponseRedirect(reverse('books'))