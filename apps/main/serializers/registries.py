from rest_framework import serializers

from main.models import File
from main.models.registries import Registries
from main.serializers.file import FileSerializer


class RegistriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registries
        fields = '__all__'

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
        # stock.text = text
        # stock.save()
        return stock

    def to_representation(self, instance):
        self.fields['file'] = FileSerializer(context=self.context)
        return super(RegistriesSerializer, self).to_representation(instance)
