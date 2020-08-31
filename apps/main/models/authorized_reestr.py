from django.db import models
from django.db.models import CASCADE

from core.django.model import BaseModel


class AuthorizedReestr(BaseModel):
    ACCREDITATION = 'accreditation'
    OK = 'ok'

    TYPE = (
        (ACCREDITATION, 'аккредитация'),
        (OK, 'одобрение'),
    )

    title_organ = models.CharField(max_length=255,
                                   verbose_name='Наименование юр. лица')

    ministry_office = models.CharField(max_length=255,
                                       verbose_name='Вазирлик, идора')

    name_of_the_conformity_assessment_body = models.CharField(max_length=255,
                                                              verbose_name='Мувофиқликни баҳолаш органи номи')
    field_of_activity = models.CharField(max_length=255,
                                         verbose_name='Фаолият соҳаси')

    the_type_document_issued = models.CharField(max_length=255,
                                                verbose_name='Мувофиқликни тасдиқлаш учун расмийлаштирадиган ҳужжат тури')

    authorized_document = models.CharField(max_length=255,
                                           verbose_name='Ваколат берилган хуқуқий ҳужжат')
    type = models.CharField(max_length=255, choices=TYPE,
                            verbose_name='Вид оценки')
    mandatory_document = models.CharField(max_length=255,
                                          verbose_name='Мажбурийлиги белгиланган ҳуқуқий ҳужжат')

    reestr = models.ForeignKey('main.Registries', CASCADE, null=True,
                               blank=True,
                               verbose_name=' Государственный реестр')
    confirm_reestr = models.ForeignKey('main.ConfirmReestr', CASCADE,
                                       null=True, blank=True,
                                       verbose_name=' Реестр одобренных лабораторий')

    def __str__(self):
        return self.title_organ

    class Meta:
        verbose_name = 'Реестр уполномоченных'
        verbose_name_plural = 'Реестр уполномоченных'
