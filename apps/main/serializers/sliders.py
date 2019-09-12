from rest_framework import serializers
from main.models.sliders import Slider


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        exclude = ['created_date']
