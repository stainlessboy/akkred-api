from django.contrib import admin
from django.http import HttpResponse

from core.printable.akkred import AkkredPDF
from core.rest_framework.printable_responses import pdf_response
from main.models import ConfirmReestr, ConfirmReestrStatus
from django.forms import Textarea
from django.db import models


def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode(
        'utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Number"),
        smart_str(u"Inn"),
        smart_str(u"title_yurd_lisa"),
        smart_str(u"title_organ"),
        smart_str(u"title_organ_type"),
        smart_str(u"address"),
        smart_str(u"address_organ"),
        smart_str(u"phone"),
        smart_str(u"email"),
        smart_str(u"web_site"),
        smart_str(u"address_organ"),
        smart_str(u"full_name_supervisor_ao"),
        smart_str(u"phone_ao"),
        smart_str(u"email_ao"),
        smart_str(u"status"),
        smart_str(u"status_date"),
        smart_str(u"accreditation_date"),
        smart_str(u"validity_date"),
        smart_str(u"reissue_date"),
        smart_str(u"designation_of_the_fundamental_standard"),
        smart_str(u"oked"),
        smart_str(u"soogu"),

        smart_str(u"Branches"),
    ])
    for obj in queryset:
        directions_list = []
        for direction in obj.directions.all():
            directions_list.append(direction.name)

        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.number),
            smart_str(obj.inn),
            smart_str(obj.title_yurd_lisa),
            smart_str(obj.title_organ),
            smart_str(obj.title_organ_type),
            smart_str(obj.address),
            smart_str(obj.address_organ),
            smart_str(obj.phone),
            smart_str(obj.email),
            smart_str(obj.web_site),
            smart_str(obj.address_organ),
            smart_str(obj.full_name_supervisor_ao),
            smart_str(obj.phone_ao),
            smart_str(obj.email_ao),
            smart_str(obj.status),
            smart_str(obj.status_date),
            smart_str(obj.accreditation_date),
            smart_str(obj.validity_date),
            smart_str(obj.reissue_date),
            smart_str(obj.designation_of_the_fundamental_standard),
            smart_str(obj.oked),
            smart_str(obj.soogu),

            smart_str(directions_list),
        ])
    return response


export_csv.short_description = u"Export CSV"


class RegistriesStatusInline(admin.TabularInline):
    model = ConfirmReestrStatus
    fields = ['date',
              'status',
              'case_type',
              'note']


@admin.register(ConfirmReestr)
class Admin(admin.ModelAdmin):
    list_display = ['title_organ']
    actions = [export_csv]
    filter_horizontal = ('directions',)
    search_fields = ['number', 'title_organ', 'inn', 'id', 'code']
    list_filter = ['region', 'status', 'is_fact_address',
                   'is_public']
    inlines = [RegistriesStatusInline]
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
