from django.contrib import admin
from men.views import *
from django.urls import path,include
from projectBin import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('men.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

handler404 = pageNotFound
handler403 = Error
handler400 = Error400

