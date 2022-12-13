from django.shortcuts import render, redirect
from book_site.models import User

def admin(request):
    return render(request, 'admin.html')

def books(request):
    return render(request, 'book.html')

def users(request):
    user = User.objects.all()

    data = {'name': user}

    return render(request, 'user.html', data)

def change(request):

    if request.method == "POST":
        role = request.POST['role']
        if role == True:
            role = False
        else:
            role = True

    return redirect('/')