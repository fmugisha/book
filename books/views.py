from django.shortcuts import render, redirect
from books.models import Books
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

def books(request):

    book = Books.objects.all()

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
    edited = Books.objects.get(id=id)
    context = {
        'bookedit': edited,
    }
    return render(request, 'book.html', context)

def editrecord(request, id):
    edited = Books.objects.get(id=id)
    edited.bookName = request.POST['ename']
    edited.bookAuthor = request.POST['eauthor']
    edited.bookDescription = request.POST['edesc']
    edited.bookTotal = request.POST['enumber']
    edited.bookImage = request.POST['eimage']
    edited.save();

    return redirect('books')