from django.db import models
from django.db.models import PROTECT

from core.django.model import BaseModel


class Document(BaseModel):
    parents = models.ForeignKey('main.DocParent', PROTECT,
                                related_name='documents', default=None)
    title = models.CharField(max_length=255)
    file = models.ForeignKey('main.File', PROTECT, related_name='documents',
                             null=True, blank=True)

    def __str__(self):
        return self.title
