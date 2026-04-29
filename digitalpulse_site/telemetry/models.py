from django.db import models

class Visit(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    path = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)


class DownloadEvent(models.Model):
    ip_address = models.GenericIPAddressField()
    version = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)