from django.db import models

def installer_upload_path(instance, filename):
    return f"installers/DigitalPulse-{instance.version}.exe"

class Release(models.Model):
    version = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    changelog = models.TextField(blank=True)

    installer = models.FileField(upload_to=installer_upload_path)

    is_latest = models.BooleanField(default=False)
    release_date = models.DateTimeField(auto_now_add=True)

    download_count = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.is_latest:
            Release.objects.exclude(id=self.id).update(is_latest=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} v{self.version}"


class Screenshot(models.Model):
    release = models.ForeignKey(Release, on_delete=models.CASCADE, related_name='screenshots')
    image = models.ImageField(upload_to='screenshots/')
    caption = models.CharField(max_length=255, blank=True)