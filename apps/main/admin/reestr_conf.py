from django.contrib import admin

from core.printable.akkred import AkkredPDF
from core.rest_framework.printable_responses import pdf_response
from main.models import ConfirmReestr


@admin.register(ConfirmReestr)
class Admin(admin.ModelAdmin):
    list_display = ['title_organ']
    search_fields = ['title_organ']
    filter_horizontal = ('directions',)
    change_form_template = "entities/change_form.html"

    fields = [
        'title_organ',
        'title_yurd_lisa',
        'address_organ',
        'address',
        'number',
        'accreditation_date',
        'validity_date',
        'reissue_date',
        'inn',
        'phone',
        'email',
        'web_site',
        'full_name_supervisor_ao',
        'is_fact_address',
        'phone_ao',
        'email_ao',
        'status',
        'status_date',
        'accreditation_duration',
        'designation_of_the_fundamental_standard',
        'directions',
        'text',
        'oked',
        'soogu',
        'region',
        'type_ownership',
        'is_public',
        'file_oblast',
        'certificate',
        'qr_code',
    ]

    def response_change(self, request, obj):
        if "_make-unique" in request.POST:
            instance = obj
            pdf_file = AkkredPDF(instance, request)
            pdf_file.generate()
            return pdf_response(pdf_file.get_output(), f' Akkred.pdf')
        return super().response_change(request, obj)
