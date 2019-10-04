from django.db import models
from django.db.models import PROTECT
from core.django.model import BaseModel
from main.models.media import Media


class Slider(BaseModel):
    title = models.CharField(max_length=255)
    image = models.ForeignKey('main.File', PROTECT, blank=True,
                              related_name='sliders')
    description = models.TextField(blank=True)
    link = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title
