from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.db.models import CASCADE
from django.utils.safestring import mark_safe
from core.django.model import BaseModel

import datetime
import uuid

from django.core.validators import RegexValidator
from django.core.validators import ValidationError as Error
from rest_framework.serializers import ValidationError

FILE_TYPES = {
    r'^(doc|docx)$': 'document',
    r'^(pdf)$': 'pdf',
    r'^(htm)$': 'htm',
    r'^(jpg|jpeg|png|gif|JPG)$': 'image',
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


class News(BaseModel):
    title = models.CharField(max_length=500, null=False)
    text = RichTextUploadingField(blank=True, null=True)
    image_main = models.ImageField(null=True, blank=True,
                                   upload_to=upload_name)
    created_date_by_admin = models.DateTimeField(null=True)

    def admin_photo(self):
        return mark_safe(
            '<img src="{}" width="100" />'.format(self.image_main.url))

    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    class Meta:
        ordering = ['-id']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
