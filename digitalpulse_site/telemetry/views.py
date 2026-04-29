# telemetry/views.py
from django.shortcuts import render
from .models import Visit, DownloadEvent

def dashboard(request):
    total_visits = Visit.objects.count()
    total_downloads = DownloadEvent.objects.count()

    return render(request, 'dashboard.html', {
        'visits': total_visits,
        'downloads': total_downloads
    })