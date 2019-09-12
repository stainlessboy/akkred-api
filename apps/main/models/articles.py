from django.db import models
from django.db.models import PROTECT

from core.django.model import BaseModel


class Articles(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey('main.File', PROTECT, related_name='articles', null=True, blank=True)
    gallery = models.ManyToManyField('main.File', related_name='gallery_articles', null=True, blank=True)

    def __str__(self):
        return self.title
