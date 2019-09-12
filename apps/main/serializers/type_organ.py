from rest_framework import serializers

from main.models import TypeOrgan


class TypeOrganModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOrgan
        fields = '__all__'
