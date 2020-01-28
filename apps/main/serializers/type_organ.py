from rest_framework import serializers

from main.models import TypeOrgan, Registries


class TypeOrganModelSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = TypeOrgan
        fields = '__all__'

    def get_attribute(self, instance):
        pass

    def get_count(self, obj):
        count = obj.registry.filter(status=Registries.ACTIVE).count()
        return count
