from django.db import models
from django.db.models import PROTECT, CASCADE


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

    title_organ = models.CharField(max_length=255)
    number = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, choices=STATUS_TYPES,
                              default=INACTIVE)
    full_name_supervisor = models.CharField(max_length=255, null=True)
    position_supervisor_legal = models.CharField(max_length=255, null=True)
    address_applicant = models.CharField(max_length=1000, null=True)
    title_applicant = models.CharField(max_length=1000, null=True)

    type_organ = models.ForeignKey('main.TypeOrgan', PROTECT,
                                   related_name='registry')
    inn = models.CharField(max_length=455, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    web_site = models.CharField(max_length=255, null=True, blank=True)
    address_organ = models.CharField(max_length=1000, null=True)
    region = models.ForeignKey('main.Region', PROTECT, null=True, blank=True)
    keywords = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    area = models.CharField(max_length=255)
    status_date = models.DateField(null=True)
    accreditation_date = models.DateField(null=True, blank=True)
    accreditation_duration = models.DateField(null=True)
    accreditation_duration_text = models.CharField(max_length=1000, null=True, blank=True)
    form_ownership = models.CharField(max_length=455)
    designation_of_the_fundamental_standard = models.CharField(max_length=455, null=True)
    file = models.ForeignKey('main.File', on_delete=CASCADE, null=True,
                             related_name='registers', blank=True)

    full_name_supervisor_ao = models.CharField(max_length=255, null=True)
    position_supervisor_ao = models.CharField(max_length=255, null=True)
    phone_ao = models.CharField(max_length=255, null=True)
    email_ao = models.CharField(max_length=255, null=True)
    web_site_ao = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title_organ
