from rest_framework import serializers
from main.models.articles import Articles


class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        exclude = ['modified_date', 'created_date']
