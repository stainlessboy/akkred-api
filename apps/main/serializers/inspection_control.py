from rest_framework import serializers
from main.models.inspection_control import InspectionControl, ICCategory


class InspectionControlTypeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    name_uz = serializers.ReadOnlyField()
    name_ru = serializers.ReadOnlyField()


class ICCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ICCategory
        fields = '__all__'


class InspectionControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectionControl
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['category'] = InspectionControlTypeSerializer()
        return super(InspectionControlSerializer, self).to_representation(
            instance)
