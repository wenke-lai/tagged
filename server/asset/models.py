from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from tag.models import Tag

User = get_user_model()


class Asset(models.Model):
    asset_id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100)
    description = models.TextField(**settings.NULLABLE)
    link = models.URLField(max_length=200, **settings.NULLABLE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
