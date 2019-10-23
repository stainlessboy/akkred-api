from collections import defaultdict

from rest_framework import serializers

from main.models.registries import Registries
from main.serializers.file import FileSerializer


class RegistriesSerializer(serializers.ModelSerializer):
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
            form_ownership=dict(required=False),
            designation_of_the_fundamental_standard=dict(required=False),
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

    def create(self, validated_data: dict):
        # file = validated_data['file']
        # validated_data.pop('text', None)
        # res = File.objects.filter(name=file).first()
        # with open(res.file.path, encoding="utf8", errors='ignore') as f:
        #     # print(f.readlines())
        #     # text = f.readlines()
        #     lines = f.readlines()
        #     text = ''.join(lines)
        # validated_data['text'] = res
        # print(validated_data['text'])
        # print(res)
        # f = open("http://localhost:8000/media/%s" % file)

        stock = super(RegistriesSerializer, self).create(validated_data)
        return stock

    def to_representation(self, instance):
        self.fields['file'] = FileSerializer(context=self.context)
        return super(RegistriesSerializer, self).to_representation(instance)
