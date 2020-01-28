from django.db import models


class DocParent(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория Документа'
        verbose_name_plural = 'Категории Документов'
