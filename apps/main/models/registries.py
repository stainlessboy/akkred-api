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

    itt_cd = models.CharField(max_length=255, null=True, blank=True)
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
    code_nd = models.ManyToManyField('main.Code', related_name='registries', blank=True)
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


class CaseType(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Причина'
        verbose_name_plural = 'Причина'


class RegisterStatusLog(models.Model):
    reestr = models.ForeignKey('main.Registries', CASCADE, related_name='reestr_logs')
    note = models.CharField(max_length=500, null=True, blank=True)
    case_type = models.ForeignKey('main.CaseType', CASCADE, related_name='reestr_logs', null=True)
    restore_date = models.DateField(null=True, blank=True)
    inactive_date = models.DateField(null=True, blank=True)
    paused_date = models.DateField(null=True, blank=True)
    extended_date = models.DateField(null=True, blank=True)
    renewal_date = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['-id']


class RegistriesStatus(models.Model):
    reestr = models.ForeignKey('main.Registries', CASCADE, related_name='reestr_status')
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    PAUSED = 'paused'
    DONE = 'done'
    RENEWED = 'renewed'
    STATUS_TYPES = (
        (ACTIVE, 'Возобновлено'),
        (INACTIVE, 'Прекращено'),
        (PAUSED, 'Приостановлено'),
        (DONE, 'Подтверждено'),
        (RENEWED, 'Переоформлено'),
    )
    status = models.CharField(max_length=20, choices=STATUS_TYPES,
                              default=INACTIVE)

    date = models.DateField(null=True)
    note = models.CharField(max_length=500, null=True, blank=True)
    case_type = models.ForeignKey('main.CaseType', CASCADE, related_name='reestr_status', null=True)


class CodeType(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


# N60368 = '60368'

class Code(models.Model):
    N060001 = '060001'
    N060002 = '060002'
    N060025 = '060025'
    N060030 = '060030'
    N060031 = '060031'
    N060043 = '060043'
    N060047 = '060047'
    N060065 = '060065'
    N060080 = '060080'
    N060085 = '060085'
    N060128 = '060128'
    N060142 = '060142'
    N060157 = '060157'
    N060168 = '060168'
    N060170 = '060170'
    N060171 = '060171'
    N060173 = '060173'
    N060174 = '060174'
    N060176 = '060176'
    N060178 = '060178'
    N060192 = '060192'
    N060237 = '060237'
    N060241 = '060241'
    N060243 = '060243'
    N060247 = '060247'
    N060256 = '060256'
    N060275 = '060275'
    N060282 = '060282'
    N060301 = '060301'
    N060319 = '060319'
    N060340 = '060340'
    N060346 = '060346'
    N060348 = '060348'
    N060349 = '060349'
    N060352 = '060352'
    N060353 = '060353'
    N060354 = '060354'
    N060357 = '060357'
    N060361 = '060361'
    N060362 = '060362'
    N060369 = '060369'
    N060373 = '060373'
    N060374 = '060374'
    N060376 = '060376'
    NMS0001 = 'ms0001'
    NMS0002 = 'ms0002'
    NMS0003 = 'ms0003'
    NMS0004 = 'ms0004'
    NMS0005 = 'ms0005'
    NMS0006 = 'ms0006'
    NMS0007 = 'ms0007'
    NMS0008 = 'ms0008'
    NMS0009 = 'ms0009'
    NMS0010 = 'ms0010'
    NMS0011 = 'ms0011'
    NMS0012 = 'ms0012'
    NMS0013 = 'ms0013'
    NMS0014 = 'ms0014'
    NMS0015 = 'ms0015'
    NMS0017 = 'ms0017'
    N60368 = '60368'

    STATUS_TYPES = (
        (N060001, '060001'),
        (N060002, '060002'),
        (N060025, '060025'),
        (N060030, '060030'),
        (N060031, '060031'),
        (N060043, '060043'),
        (N060047, '060047'),
        (N060065, '060065'),
        (N060080, '060080'),
        (N060085, '060085'),
        (N060128, '060128'),
        (N060142, '060142'),
        (N060157, '060157'),
        (N060168, '060168'),
        (N060170, '060170'),
        (N060171, '060171'),
        (N060173, '060173'),
        (N060174, '060174'),
        (N060176, '060176'),
        (N060178, '060178'),
        (N060192, '060192'),
        (N060237, '060237'),
        (N060241, '060241'),
        (N060243, '060243'),
        (N060247, '060247'),
        (N060256, '060256'),
        (N060275, '060275'),
        (N060282, '060282'),
        (N060301, '060301'),
        (N060319, '060319'),
        (N060340, '060340'),
        (N060346, '060346'),
        (N060348, '060348'),
        (N060349, '060349'),
        (N060352, '060352'),
        (N060353, '060353'),
        (N060354, '060354'),
        (N060357, '060357'),
        (N060361, '060361'),
        (N060362, '060362'),
        (N060369, '060369'),
        (N060373, '060373'),
        (N060374, '060374'),
        (N60368, '60368'),
        (N060376, '060376'),
        (NMS0001, 'ms0001'),
        (NMS0002, 'ms0002'),
        (NMS0003, 'ms0003'),
        (NMS0004, 'ms0004'),
        (NMS0005, 'ms0005'),
        (NMS0006, 'ms0006'),
        (NMS0007, 'ms0007'),
        (NMS0008, 'ms0008'),
        (NMS0009, 'ms0009'),
        (NMS0010, 'ms0010'),
        (NMS0011, 'ms0011'),
        (NMS0012, 'ms0012'),
        (NMS0013, 'ms0013'),
        (NMS0014, 'ms0014'),
        (NMS0015, 'ms0015'),
        (NMS0017, 'ms0017'),

    )

    cod_tnved = models.CharField(max_length=500)
    organ_number = models.CharField(max_length=50, choices=STATUS_TYPES)

    def __str__(self):
        return self.cod_tnved
