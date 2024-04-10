from django.conf import settings
from django.db import models


class Asset(models.Model):
    asset_id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100)
    description = models.TextField(**settings.NULLABLE)
    link = models.URLField(max_length=200, **settings.NULLABLE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
