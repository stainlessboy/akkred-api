from django.contrib import admin
from django.http import HttpResponse
from reportlab import xrange

from main.models import Registries \
    , RegistriesStatus


def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))  # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        smart_str(u"Number"),
        smart_str(u"Itt cd"),
        smart_str(u"Inn"),
        smart_str(u"title_yurd_lisa"),
        smart_str(u"address_yurd_lisa"),
        smart_str(u"phone"),
        smart_str(u"email"),
        smart_str(u"web_site"),
        smart_str(u"type_organ"),
        smart_str(u"title_organ"),
        smart_str(u"address_organ"),
        smart_str(u"full_name_supervisor_ao"),
        smart_str(u"phone_ao"),
        smart_str(u"email_ao"),
        smart_str(u"status"),
        smart_str(u"status_date"),
        smart_str(u"accreditation_date"),
        smart_str(u"accreditation_duration"),
        smart_str(u"accreditation_duration_text"),
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
            smart_str(obj.itt_cd),
            smart_str(obj.inn),
            smart_str(obj.title_yurd_lisa),
            smart_str(obj.address_yurd_lisa),
            smart_str(obj.phone),
            smart_str(obj.email),
            smart_str(obj.web_site),
            smart_str(obj.type_organ.name),
            smart_str(obj.title_organ),
            smart_str(obj.address_organ),
            smart_str(obj.full_name_supervisor_ao),
            smart_str(obj.phone_ao),
            smart_str(obj.email_ao),
            smart_str(obj.status),
            smart_str(obj.status_date),
            smart_str(obj.accreditation_date),
            smart_str(obj.accreditation_duration),
            smart_str(obj.accreditation_duration_text),
            smart_str(obj.designation_of_the_fundamental_standard),
            smart_str(obj.oked),
            smart_str(obj.soogu),

            smart_str(directions_list),
        ])
    return response


export_csv.short_description = u"Export CSV"


# def export_xls(modeladmin, request, queryset):
#     import xlwt
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename=reestr.xls'
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet("MyModel")
#
#     row_num = 0
#
#     columns = [
#         (u"number", 6000),
#         (u"title_organ", 8000),
#         (u"directions", 8000),
#     ]
#
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#
#     for col_num in xrange(len(columns)):
#         ws.write(row_num, col_num, columns[col_num][0], font_style)
#         # set column width
#         ws.col(col_num).width = columns[col_num][1]
#
#     font_style = xlwt.XFStyle()
#     font_style.alignment.wrap = 1
#
#     for obj in queryset:
#         row_num += 1
#         row = [
#             obj.number,
#             obj.type_organ.title,
#             obj.directions.all(),
#         ]
#         for col_num in xrange(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)
#
#     wb.save(response)
#     return response


# export_xls.short_description = u"Export XLS"


class RegistriesStatusInline(admin.TabularInline):
    model = RegistriesStatus
    fields = ['date',
              'status',
              'case_type',
              'note']


@admin.register(Registries)
class Admin(admin.ModelAdmin):
    actions = [export_csv]
    filter_horizontal = ('code_nd', 'directions')
    list_display = ['title_organ', 'type_organ', 'number']
    search_fields = ['number', 'title_organ', 'inn', 'id', 'code']
    list_filter = ['region', 'type_organ', 'status', 'is_fact_address', 'accreditation_date']
    inlines = [RegistriesStatusInline]
