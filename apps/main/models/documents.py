from django.db.models import PROTECT

from core.django.model import BaseModel

import datetime
import uuid

from django.core.validators import RegexValidator
from django.core.validators import ValidationError as Error
from django.db import models
from rest_framework.serializers import ValidationError

FILE_TYPES = {
    r'^(doc|docx)$': 'document',
    r'^(pdf)$': 'pdf',
    r'^(htm)$': 'htm',
    r'^(jpg|jpeg|png|gif)$': 'image',
    r'^(xls|xlsx)$': 'excel',
    r'^(zip|rar)$': 'compressed',
}


def upload_name(instance, filename):
    file_type = filename.split('.')[-1]
    today = str(datetime.datetime.today())[0:7]
    for regex, folder in FILE_TYPES.items():
        try:
            RegexValidator(regex).__call__(file_type)
            return 'file/%s/%s/%s.%s' % (
                folder, today, uuid.uuid4(), file_type)
        except Error:
            pass
    raise ValidationError(detail={'File type is unacceptable'})


class Document(BaseModel):
    FILE = 'file'
    LINK = 'link'
    STATUS_TYPES = (

        (FILE, 'file'),
        (LINK, 'link'),
    )
    status = models.CharField(max_length=20, choices=STATUS_TYPES,
                              default=LINK)

    parents = models.ForeignKey('main.DocParent', PROTECT,
                                related_name='documents', default=None)
    type = models.ForeignKey('main.DocType', PROTECT,
                             related_name='documents', default=None, null=True, blank=True)

    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    number = models.CharField(max_length=300, null=True)
    link = models.CharField(max_length=300, null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    file = models.FileField(upload_to=upload_name, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class DocumentForm(models.Model):
    document = models.ForeignKey('main.Document', PROTECT,
                                 related_name='document_forms')
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=upload_name, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['order']
        verbose_name = 'Форма Документа '
        verbose_name_plural = 'Форма Документа'
