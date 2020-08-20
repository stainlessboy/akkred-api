from django.contrib import admin

from core.printable.akkred import AkkredPDF
from core.rest_framework.printable_responses import pdf_response
from main.models import ConfirmReestr
from django.forms import TextInput, Textarea
from django.db import models


@admin.register(ConfirmReestr)
class Admin(admin.ModelAdmin):
    list_display = ['title_organ']
    search_fields = ['title_organ']
    filter_horizontal = ('directions',)
    change_form_template = "entities/change_form.html"

    fields = [
        'area',
        'number',
        'inn',
        'oked',
        'soogu',
        'title_organ',
        'title_yurd_lisa',
        'title_organ_type',
        'title_organ_short',
        'address_organ',
        'address',
        'phone',
        'email',
        'web_site',
        'full_name_supervisor_ao',
        'is_fact_address',
        'phone_ao',
        'email_ao',
        'status',
        'status_date',
        'accreditation_date',
        'validity_date',
        'reissue_date',
        'is_reissue_date',
        'designation_of_the_fundamental_standard',
        'directions',
        'text',
        'region',
        'type_ownership',
        'file_oblast',
        'certificate',
        'qr_code',
        'is_public',

    ]

    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 4, 'cols': 40})},
    }

    def response_change(self, request, obj):
        if "_make-unique" in request.POST:
            instance = obj
            pdf_file = AkkredPDF(instance, request)
            pdf_file.generate()
            return pdf_response(pdf_file.get_output(), f' Akkred.pdf')
        return super().response_change(request, obj)
