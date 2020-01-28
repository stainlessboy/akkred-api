import datetime
import uuid

from django.core.validators import RegexValidator
from django.core.validators import ValidationError as Error
from django.db import models
from django.utils.safestring import mark_safe
from rest_framework.serializers import ValidationError

from core.django.model import BaseModel, DeleteModel

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


class MediaFile(models.Model):
    file = models.FileField(upload_to=upload_name)
    name = models.CharField(max_length=255, null=True)

    def link(self):
        return mark_safe('<a>http://test.akkred.uz/{}</a>'.format(self.file.url))

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.file.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    link.short_description = 'link'
    link.allow_tags = True

    def __str__(self):
        return f'id={self.id}'

    class Meta:
        verbose_name = 'Библиотека файлов'
        verbose_name_plural = 'Библиотека фалов'
