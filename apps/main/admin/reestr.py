from django.contrib import admin
from django.http import HttpResponse
from reportlab import xrange

from main.models import Registries \
    , RegisterStatusLog


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
        smart_str(u"Code"),
    ])
    for obj in queryset:
        writer.writerow([
            smart_str(obj.pk),
            smart_str(obj.number),
            smart_str(obj.text),
        ])
    return response


export_csv.short_description = u"Export CSV"


def export_xls(modeladmin, request, queryset):
    import xlwt
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=reestr.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("MyModel")

    row_num = 0

    columns = [
        (u"number", 6000),
        (u"title_organ", 8000),
    ]

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]

    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    for obj in queryset:
        row_num += 1
        row = [
            obj.number,
            obj.title_organ,
        ]
        for col_num in xrange(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


export_xls.short_description = u"Export XLS"


class RegistriesStatusInline(admin.TabularInline):
    model = RegisterStatusLog
    fields = [
        'paused_date',
        'restore_date',
        'inactive_date',
        'extended_date',
        'renewal_date',
        'case_type',
        'note',

    ]


@admin.register(Registries)
class Admin(admin.ModelAdmin):
    actions = [export_xls, export_csv]
    list_display = ['title_organ', 'type_organ', 'number']
    search_fields = ['number', 'title_organ', 'inn', 'id']
    list_filter = ['region', 'type_organ', 'status', 'is_fact_address', 'accreditation_date']
    inlines = [RegistriesStatusInline]
