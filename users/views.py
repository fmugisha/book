from django.shortcuts import render, redirect
from book_site.models import User

def users(request):
    user = User.objects.all()

    data = {'name': user}

    return render(request, 'user.html', data)

def change(request, id):
    admin = User.objects.get(id=id)
    if request.method == "POST":
        if User.role == True:
            User.role = False
        elif User.role == False:
            User.role = True
    admin.save();
    return redirect('/')