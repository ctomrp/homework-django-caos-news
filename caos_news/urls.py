from django.contrib import admin
from django.urls import path, include
from core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('register/',views.auth_register),
    #path('login/',views.auth_login),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)