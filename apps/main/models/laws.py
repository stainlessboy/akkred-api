from django.db import models
from django.db.models import CASCADE


class LawsCategory(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Laws(models.Model):
    category = models.ForeignKey('main.LawsCategory', CASCADE, related_name='laws')
    name = models.TextField()
    name2 = models.TextField()
    link = models.CharField(max_length=300)

    def __str__(self):
        return self.name
