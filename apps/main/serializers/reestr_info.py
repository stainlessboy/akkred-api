from rest_framework import serializers

from main.models.reestr_info_user import ReestrInfoUser


class ReestrInfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReestrInfoUser
        fields = '__all__'
