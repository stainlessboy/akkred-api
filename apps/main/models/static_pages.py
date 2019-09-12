from django.db import models

from core.django.model import BaseModel


class StaticPage(BaseModel):
    key_name = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
