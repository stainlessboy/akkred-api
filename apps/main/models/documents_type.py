from django.db import models


class DocType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип Документа'
        verbose_name_plural = 'Типы Документов'
