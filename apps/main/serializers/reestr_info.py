from collections import defaultdict

from rest_framework import serializers

from main.models.reestr_info_user import ReestrInfoUser
from main.serializers.file import FileSerializer


class ReestrInfoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReestrInfoUser
        fields = '__all__'
