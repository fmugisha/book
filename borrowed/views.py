from django.shortcuts import render

# Create your views here.
def borrowed(request):
    return render(request, 'bor.html')