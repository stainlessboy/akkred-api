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
    TEMPORARILY_RESUMED = 'temporarily_resumed'

    STATUS_TYPES = (
        (ACTIVE, 'Действующий'),
        (INACTIVE, 'Прекращен'),
        (PAUSED, 'Приостановлен'),
        (EXTENDED, 'Продлен'),
        (TEMPORARILY_RESUMED, 'Временно возобновлен'),
    )

    PUBLIC = 'public'
    PRIVATE = 'private'

    TYPE_OWNERSHIP = (
        (PUBLIC, 'государственный'),
        (PRIVATE, 'частный'),
    )

    title_yurd_lisa = models.CharField(max_length=1000, null=True,
                                       verbose_name='sinov laboratoriyasi nomi')
    title_organ = models.CharField(max_length=255,
                                   verbose_name='Yuridik shaxs nomi')
    title_organ_type = models.CharField(max_length=255,
                                        verbose_name='Yuridik shaxs mulkchilik shakli',
                                        null=True)

    address = models.CharField(max_length=255, null=True,
                               verbose_name='Joylashgan manzil')

    address_organ = models.CharField(max_length=1000, null=True,
                                     verbose_name='Yuridik manzil')

    number = models.CharField(max_length=255, null=True,
                              verbose_name="Reestrda ro'yxat raqami")

    accreditation_date = models.DateField(null=True,
                                          verbose_name="Reestrda ro'yxatga olingan sana")
    validity_date = models.DateField(null=True,
                                     verbose_name='Amal qilish muddati')

    reissue_date = models.DateField(null=True,
                                    verbose_name='Qayta rasmiylashtirilgan sana')

    # TODO
    inn = models.CharField(max_length=455, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    web_site = models.CharField(max_length=255, null=True, blank=True)
    full_name_supervisor_ao = models.CharField(max_length=255, null=True)
    is_fact_address = models.BooleanField(default=False)
    phone_ao = models.CharField(max_length=255, null=True, blank=True)
    email_ao = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_TYPES,
                              default=INACTIVE)
    status_date = models.DateField(null=True)

    # TODO PUBLIC
    designation_of_the_fundamental_standard = models.CharField(max_length=455,
                                                               null=True)
    directions = models.ManyToManyField('main.Directions', blank=True)
    text = models.TextField(null=True, blank=True)
    oked = models.CharField(max_length=255, null=True, blank=True)
    soogu = models.CharField(max_length=255, null=True, blank=True)

    file_oblast = models.FileField(upload_to=upload_name, null=True,
                                   blank=True)
    region = models.ForeignKey('main.Region', PROTECT, null=True, blank=True)
    type_ownership = models.CharField(max_length=45, choices=TYPE_OWNERSHIP,
                                      null=True, blank=True)

    is_public = models.BooleanField(default=True)
    qr_code = models.ImageField(null=True, blank=True,
                                upload_to=upload_name)
    certificate = models.FileField(upload_to=upload_name, null=True,
                                   blank=True)
    area = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.title_organ

    class Meta:
        verbose_name = 'Реестр одобренных лабораторий'
        verbose_name_plural = 'Реестр одобренных лабораторий'
