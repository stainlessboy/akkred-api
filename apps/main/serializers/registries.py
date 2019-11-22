from collections import defaultdict

from rest_framework import serializers

from main.models.registries import Registries
from main.serializers.file import FileSerializer


class OptionsValueSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    status = serializers.CharField(required=False)
    date = serializers.DateField(required=False)


class RegistriesSerializer(serializers.ModelSerializer):
    reestr_status = OptionsValueSerializer(many=True, required=False)

    class Meta:
        model = Registries
        fields = '__all__'
        extra_kwargs = dict(
            area=dict(required=True),
            number=dict(required=False),
            code=dict(required=False),
            email=dict(required=False),
            address=dict(required=False),
            text=dict(required=False),
        )

    def validate(self, attrs):
        errors = defaultdict(list)
        area = attrs.get('area')
        if not self.instance and Registries.objects.filter(area=area).exists():
            errors['non_field_errors'].append(
                'You can not create reestr with area')
        if self.instance.area != area and Registries.objects.filter(area=area).exists():
            errors['non_field_errors'].append(
                'You can not create reestr with area')

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    # def to_representation(self, instance):
    #     self.fields['file'] = FileSerializer(context=self.context)
    #     return super(RegistriesSerializer, self).to_representation(instance)


class RegistriesSearchSerializer(serializers.Serializer):
    search_name = serializers.CharField(source='title_organ__icontains', required=False)
    # search_description = serializers.CharField(source='description__icontains', required=False)
