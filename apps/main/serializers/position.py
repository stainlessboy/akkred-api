from rest_framework import serializers
from django.contrib.auth.models import Group


class PermissionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    codename = serializers.ReadOnlyField()


class GroupSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    permissions = PermissionSerializer(many=True, read_only=True)


class PositionSelectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()


class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'permissions'
        ]

    def to_representation(self, instance):
        self.fields['permissions'] = PermissionSerializer(many=True, read_only=True)
        return super(GroupModelSerializer, self).to_representation(instance)
