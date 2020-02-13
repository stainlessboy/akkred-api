from django.db.models import PROTECT, CASCADE
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


class Registries(models.Model):
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
    address_yurd_lisa = models.CharField(max_length=1000, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    web_site = models.CharField(max_length=255, null=True, blank=True)
    type_organ = models.ForeignKey('main.TypeOrgan', PROTECT,
                                   related_name='registry')
    title_organ = models.CharField(max_length=255)
    address_organ = models.CharField(max_length=1000, null=True)
    full_name_supervisor_ao = models.CharField(max_length=255, null=True)

    is_fact_address = models.BooleanField(default=False)
    phone_ao = models.CharField(max_length=255, null=True, blank=True)
    email_ao = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_TYPES,
                              default=INACTIVE)
    status_date = models.DateField(null=True)
    accreditation_date = models.DateField(null=True)
    accreditation_duration = models.DateField(null=True, blank=True)
    accreditation_duration_text = models.CharField(max_length=1000, null=True, blank=True)
    designation_of_the_fundamental_standard = models.CharField(max_length=455, null=True)

    code = models.CharField(max_length=255, null=True)

    region = models.ForeignKey('main.Region', PROTECT, null=True, blank=True)
    keywords = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    area = models.CharField(max_length=255, unique=True)

    file_oblast = models.FileField(upload_to=upload_name, null=True, blank=True)
    certificate = models.FileField(upload_to=upload_name, null=True, blank=True)

    def __str__(self):
        return self.title_organ

    class Meta:
        verbose_name = 'Государственный реестр аккредитованных ООС и МС'
        verbose_name_plural = 'Государственный реестр аккредитованных ООС и МС'


class RegisterStatusLog(models.Model):
    reestr = models.ForeignKey('main.Registries', CASCADE, related_name='reestr_logs')
    case = models.TextField()
    restore_date = models.DateField(null=True, blank=True)
    inactive_date = models.DateField(null=True, blank=True)
    paused_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-id']


class RegistriesStatus(models.Model):
    reestr = models.ForeignKey('main.Registries', CASCADE, related_name='reestr_status')
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
    status = models.CharField(max_length=20, choices=STATUS_TYPES,
                              default=INACTIVE)

    date = models.DateField(null=True)
