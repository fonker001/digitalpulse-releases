from django.contrib import admin
from django.urls import path
from core.views import home
from releases.views import download_latest
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  # ← THIS LINE FIXES YOUR ERROR

    path('', home, name='home'),
    path('download/', download_latest, name='download_latest'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)