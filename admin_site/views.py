from django.shortcuts import render
from book_site.models import User

# Create your views here.
from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request, 'admin.html')

def books(request):
    return render(request, 'book.html')

def users(request):
    user = User.objects.all()

    return render(request, 'user.html', {'name': user})