from rest_framework import serializers
from main.models.sliders import Slider
from main.serializers.file import FileSerializer


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ['description']


    def to_representation(self, instance):
        self.fields['image'] = FileSerializer(context=self.context)
        # self.fields['gallery'] = FileSerializer(context=self.context)
        return super().to_representation(instance)
