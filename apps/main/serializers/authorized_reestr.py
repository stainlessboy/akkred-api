from rest_framework import serializers

from main.models.authorized_reestr import AuthorizedReestr


class ReestrSelectSerializer(serializers.Serializer):
    area = serializers.ReadOnlyField()
    number = serializers.ReadOnlyField()


class AuthorizedReestrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedReestr
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['reestr'] = ReestrSelectSerializer(required=False)
        self.fields['confirm_reestr'] = ReestrSelectSerializer(required=False)
        return super().to_representation(instance)
