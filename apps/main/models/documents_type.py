from django.db import models


class DocType(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = 'Тип Документа'
        verbose_name_plural = 'Типы Документов'
