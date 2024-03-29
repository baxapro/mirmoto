from django.contrib import admin
from men.views import *
from django.urls import path,include
from projectBin import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/',include('captcha.urls')),
    path('',include('men.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

handler404 = pageNotFound
handler403 = Error
handler400 = Error400

