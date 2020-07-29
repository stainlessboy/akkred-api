from django.contrib import admin

from core.printable.akkred import AkkredPDF
from core.rest_framework.printable_responses import pdf_response
from main.models import ConfirmReestr


@admin.register(ConfirmReestr)
class Admin(admin.ModelAdmin):
    list_display = ['title_organ']
    search_fields = ['title_organ']
    change_form_template = "entities/change_form.html"

    def response_change(self, request, obj):
        if "_make-unique" in request.POST:
            instance = obj
            pdf_file = AkkredPDF(instance, request)
            pdf_file.generate()
            return pdf_response(pdf_file.get_output(), f' Akkred.pdf')
        return super().response_change(request, obj)
