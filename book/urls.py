from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('book_site.urls')),
    path('home/', include('home.urls')),
    path('admin/', include('admin_site.urls')),
]