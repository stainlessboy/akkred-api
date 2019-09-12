from rest_framework import serializers

from main.models import StaticPage


class StaticPageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticPage
        exclude = ['modified_date']

