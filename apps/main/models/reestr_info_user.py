from django.db import models
from django.db.models import PROTECT

from core.django.model import BaseModel


class CategoryReestrInfoUser(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ReestrInfoUser(BaseModel):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PAUSED = 'paused'
    EXTENDED = 'extended'

    STATUS_TYPES = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
        (PAUSED, 'paused'),
        (EXTENDED, 'extended'),
    )
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    date = models.DateTimeField()
    status = models.CharField(max_length=45, choices=STATUS_TYPES)
    type = models.ForeignKey('main.CategoryReestrInfoUser',PROTECT,related_name='info_reestrs')

    def __str__(self):
        return self.title
