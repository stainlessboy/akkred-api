from django.contrib import admin
from main.models import SatisfactionQuestionnaire


@admin.register(SatisfactionQuestionnaire)
class Admin(admin.ModelAdmin):
    list_display = ['questionnaire']
    search_fields = ['questionnaire']
