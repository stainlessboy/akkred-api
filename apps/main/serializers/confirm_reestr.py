from rest_framework import serializers

from main.models.confirm_reestr import ConfirmReestr


class ConfirmReestrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfirmReestr
        fields = '__all__'
