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

    title = models.CharField(max_length=255)
    number = models.CharField(max_length=255, null=True)
    code = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=20, choices=STATUS_TYPES,
                              default=INACTIVE)
    full_name = models.CharField(max_length=255, null=True)

    type_organ = models.ForeignKey('main.TypeOrgan', PROTECT,
                                   related_name='registry')
    inn = models.CharField(max_length=455, null=True)
    phone = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    region = models.ForeignKey('main.Region', PROTECT, null=True, blank=True)
    keywords = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    area = models.CharField(max_length=255)
    status_date = models.DateField(null=True)
    accreditation_date = models.DateField(null=True)
    accreditation_duration = models.DateField(null=True)
    form_ownership = models.CharField(max_length=455)
    designation_of_the_fundamental_standard = models.CharField(max_length=455,null=True)
    file = models.ForeignKey('main.File', on_delete=CASCADE, null=True,
                             related_name='registers')

    def __str__(self):
        return self.title
