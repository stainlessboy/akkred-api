from django.db import models
from django.db.models import CASCADE

from core.django.model import BaseModel
from ckeditor.fields import RichTextField

import datetime
import uuid

from django.core.validators import RegexValidator
from django.core.validators import ValidationError as Error
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


class News(BaseModel):
    title = models.CharField(max_length=255, null=False)
    text = RichTextField(blank=True, null=True)
    image_main = models.ImageField(null=True, blank=True, upload_to=upload_name)
    photo = models.ForeignKey('main.File', CASCADE, null=True,
                              related_name='new', blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title


class NewsGallery(models.Model):
    news = models.ForeignKey('main.News', CASCADE, related_name='images')
    image = models.ImageField(null=True, blank=True, upload_to=upload_name)
