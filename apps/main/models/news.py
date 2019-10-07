from django.db import models
from django.db.models import CASCADE

from core.django.model import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=255, null=False)
    text = models.TextField()
    photo = models.ForeignKey('main.File', CASCADE, null=True,
                              related_name='new', blank=True)
    gallery = models.ManyToManyField('main.File')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
