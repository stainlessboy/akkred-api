from core.django.model import BaseModel
from django.db import models
from django.db.models import PROTECT


class Employee(BaseModel):
    name = models.CharField(max_length=255, null=False, )
    position = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=255,blank=True, null=True)
    email = models.CharField(max_length=255,blank=True, null=True)
    image = models.ForeignKey('main.File', PROTECT, related_name='employees')

    def __str__(self):
        return self.name
