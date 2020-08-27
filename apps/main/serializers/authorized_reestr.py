from rest_framework import serializers

from main.models.authorized_reestr import AuthorizedReestr


class AuthorizedReestrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedReestr
        fields = '__all__'
