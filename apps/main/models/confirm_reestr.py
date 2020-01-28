from core.django.model import BaseModel
from django.db.models import PROTECT
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


class ConfirmReestr(BaseModel):
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PAUSED = 'paused'
    EXTENDED = 'extended'

    STATUS_TYPES = (
        (ACTIVE, 'active'),
        (INACTIVE, 'inactive'),
        (PAUSED, 'paused'),
        (EXTENDED, 'extended'),
    )
    number = models.CharField(max_length=255, null=True)
    inn = models.CharField(max_length=455, null=True)
    title_yurd_lisa = models.CharField(max_length=1000, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    web_site = models.CharField(max_length=255, null=True, blank=True)
    type_organ = models.ForeignKey('main.TypeOrgan', PROTECT,
                                   related_name='confirm_reestrs')
    title_organ = models.CharField(max_length=255)
    type_organ_title = None
    address_organ = models.CharField(max_length=1000, null=True)
    addres_organ_yurdn_lisa = None
    accreditation_date = models.DateField(null=True)
    full_name_supervisor_ao = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, choices=STATUS_TYPES,
                              default=INACTIVE)
    region = models.ForeignKey('main.Region', PROTECT, null=True, blank=True, related_name='confirm_reestrs')
    podpisal = models.CharField(max_length=400)
    text = models.TextField(null=True, blank=True)
    file_oblast = models.FileField(upload_to=upload_name, null=True, blank=True)

    def __str__(self):
        return self.title_organ

    class Meta:
        verbose_name = 'Реестр одобренных лабораторий'
        verbose_name_plural = 'Реестр одобренных лабораторий'
