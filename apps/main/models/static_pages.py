from django.db import models

from core.django.model import BaseModel


class StaticPage(BaseModel):
    ABOUT = 'about'
    ACTION = 'action'
    DOCUMENTATION = 'documentation'
    INFORMATION = 'information'
    APPLY = 'apply'
    CONTACT = 'contact'

    STATUS_TYPES = (
        (ABOUT, 'about'),
        (ACTION, 'action'),
        (DOCUMENTATION, 'documentation'),
        (INFORMATION, 'information'),
        (APPLY, 'apply'),
        (CONTACT, 'contact'),
    )

    key_name = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=400, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=255, choices=STATUS_TYPES,
                            default=ABOUT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
