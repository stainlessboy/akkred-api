from collections import defaultdict

from rest_framework import serializers

from main.models.registries import Registries, RegistriesStatus
from main.serializers.type_organ import TypeSelectSerializer


class StatusValueSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    status = serializers.CharField(required=False)
    date = serializers.DateField(required=False)


class RegistriesSelectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title_organ = serializers.ReadOnlyField()
    number = serializers.ReadOnlyField()


class CodeNvdSelectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    cod_tnved = serializers.ReadOnlyField()
    organ_number = serializers.ReadOnlyField()


class RegistriesSerializer(serializers.ModelSerializer):
    reestr_status = StatusValueSerializer(many=True, required=False)

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
        if self.instance.area != area and Registries.objects.filter(
                area=area).exists():
            errors['non_field_errors'].append(
                'You can not create reestr with area')

        if errors:
            raise serializers.ValidationError(errors)

        return attrs

    def to_representation(self, instance):
        self.fields['code_nd'] = CodeNvdSelectSerializer(many=True,
                                                         required=False)
        self.fields['type_organ'] = TypeSelectSerializer()
        return super(RegistriesSerializer, self).to_representation(instance)


class RegistriesSearchSerializer(serializers.Serializer):
    search_number = serializers.CharField(source='number__icontains',
                                          required=False)
    search_inn = serializers.CharField(source='inn__icontains', required=False)
    search_code = serializers.CharField(source='text__icontains',
                                        required=False)
    search_title = serializers.CharField(source='title_organ__icontains',
                                         required=False)


class RegistriesConfirmSearchSerializer(serializers.Serializer):
    search_number = serializers.CharField(source='number__icontains',
                                          required=False)
    search_inn = serializers.CharField(source='inn__icontains', required=False)


class RegistriesStatusSearchSerializer(serializers.Serializer):
    search_number = serializers.CharField(source='reestr__number__icontains',
                                          required=False)
    search_title = serializers.CharField(
        source='reestr__title_organ__icontains', required=False)


class RegistriesStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistriesStatus
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['reestr'] = RegistriesSelectSerializer()
        return super(RegistriesStatusSerializer, self).to_representation(
            instance)
