from rest_framework import serializers
from main.models.documents import CategoryDocumentForm


class CategoryDocumentFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryDocumentForm
        fields = '__all__'
