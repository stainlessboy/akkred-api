from django.db import models


class TypeOrgan(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Орган'
        verbose_name_plural = 'Орган'
