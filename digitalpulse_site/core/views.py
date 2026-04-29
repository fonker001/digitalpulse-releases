from django.shortcuts import render
from releases.models import Release

def home(request):
    latest = Release.objects.filter(is_latest=True).first()
    releases = Release.objects.all().order_by('-release_date')[:5]

    return render(request, 'home.html', {
        'latest': latest,
        'releases': releases
    })