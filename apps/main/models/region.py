from django.db import models
from core.django.model import BaseModel


class Region(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'
