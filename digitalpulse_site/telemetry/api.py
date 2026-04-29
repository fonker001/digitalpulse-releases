# telemetry/api.py
from django.http import JsonResponse
from .models import DownloadEvent

def app_ping(request):
    version = request.GET.get('version')

    DownloadEvent.objects.create(
        ip_address=request.META.get('REMOTE_ADDR'),
        version=version
    )

    return JsonResponse({'status': 'ok'})