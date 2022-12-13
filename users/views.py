from django.shortcuts import render, redirect
from book_site.models import User

def users(request):
    user = User.objects.all()

    data = {'name': user}

    return render(request, 'user.html', data)

def change(request, pk):

    if request.method == "POST":
        role = request.POST['role']
        if role.checked:
            role.update = False
            role.save();
        elif role == False:
            role = True
            role.save();


    return redirect('/')