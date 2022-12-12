from django.shortcuts import render, redirect
from django.contrib import messages
from book_site.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == "POST":
        firstName = request.POST['firstName']
        secondName = request.POST['secondName']
        gender = request.POST['gender']
        phoneNumber = request.POST['phoneNumber']
        national_ID = request.POST['national_ID']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        role = False

        if password == confirmPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'This email is taken!')
                return redirect('/')
            else:
                user = User(firstName=firstName, secondName=secondName, gender=gender,phoneNumber=phoneNumber, national_ID=national_ID, email=email, password=password, role=role)
                user.save();
                messages.info(request, 'Account created')
        else:
            messages.info(request, 'Passwords are not matching...')
            return redirect('signup')
        return redirect('/')
    else:
        return redirect('/')