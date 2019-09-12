from django.db import models


class TypeOrgan(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
