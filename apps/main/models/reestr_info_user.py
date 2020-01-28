from django.db import models
from django.db.models import PROTECT

from core.django.model import BaseModel


class CategoryReestrInfoUser(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория П.П.В'
        verbose_name_plural = 'Категория П.П.В'


class ReestrInfoUser(BaseModel):
    title = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    type = models.ForeignKey('main.CategoryReestrInfoUser', PROTECT, related_name='info_reestrs', null=True)
    date_paused = models.DateField(null=True)
    date_active = models.DateField(null=True)
    date_inactive = models.DateField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Информация о приостановленных, прекрашенных и возобновленных свидетельствах об аккредитации'
        verbose_name_plural = 'Информация о приостановленных, прекрашенных и возобновленных свидетельствах об аккредитации'
