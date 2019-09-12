from core.django.model import BaseModel
from django.db import models
from django.db.models import PROTECT


class Review(BaseModel):
    author = models.CharField(max_length=255, null=False, )
    position = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    image = models.ForeignKey('main.File', PROTECT, related_name='reviews')

    def __str__(self):
        return self.author
