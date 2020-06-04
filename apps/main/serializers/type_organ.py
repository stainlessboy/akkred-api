from rest_framework import serializers

from main.models import TypeOrgan, Registries


class TypeSelectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()
    name_en = serializers.ReadOnlyField()
    name_ru = serializers.ReadOnlyField()
    name_uz = serializers.ReadOnlyField()


class TypeOrganModelSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()

    class Meta:
        model = TypeOrgan
        fields = '__all__'

    def get_attribute(self, instance):
        pass

    def get_count(self, obj):
        count = obj.registry.filter(status__in=[Registries.ACTIVE, Registries.EXTENDED]).count()
        return count
