from django.db import models
from django.db.models import PROTECT

from core.django.model import BaseModel


class Document(BaseModel):
    parents = models.ForeignKey('main.DocParent', PROTECT,
                                related_name='documents', default=None)
    type = models.ForeignKey('main.DocType', PROTECT,
                             related_name='documents', default=None, null=True, blank=True)

    title = models.CharField(max_length=255)
    number = models.CharField(max_length=300, null=True)

    file = models.ForeignKey('main.File', PROTECT, related_name='documents',
                             null=True, blank=True)

    def __str__(self):
        return self.title
