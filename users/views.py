from django.shortcuts import render, redirect
from book_site.models import User
from django.template import loader


def users(request):
    user = User.objects.all()

    data = {"name": user}

    return render(request, "user.html", data)


def change(request, id):
    # act = request.POST['role']
    admin = User.objects.get(id=id)
    # admin.role = act
    if request.method == "POST":
        if admin.role == True:
            admin.role = False
        elif admin.role == False:
            admin.role = True
    admin.save()
    return redirect("users")
