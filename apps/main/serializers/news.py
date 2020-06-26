from rest_framework import serializers

from main.models import News


class NewsModelSerializer(serializers.ModelSerializer):
    created_date_by_admin = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = News
        fields = '__all__'
