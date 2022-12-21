from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include('book_site.urls')),
    path('home/', include('home.urls')),
    path('admin/', include('admin_site.urls')),
    path('books/', include('books.urls')),
    path('users/', include('users.urls')),
    path('borrowed/', include('borrowed.urls')),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)