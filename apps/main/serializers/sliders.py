from rest_framework import serializers
from main.models.sliders import Slider
from main.serializers.file import FileSerializer


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ['description']
