from django.shortcuts import get_object_or_404, redirect
from .models import Release
from telemetry.models import DownloadEvent

def download_latest(request):
    release = Release.objects.filter(is_latest=True).first()

    if not release:
        return redirect('/')

    ip = request.META.get('REMOTE_ADDR')

    # Track download
    DownloadEvent.objects.create(
        ip_address=ip,
        version=release.version
    )

    # Increment counter
    release.download_count += 1
    release.save()

    return redirect(release.installer.url)