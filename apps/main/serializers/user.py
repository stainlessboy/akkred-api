from collections import defaultdict
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers, viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from main.models import User

#
# from main.models import User, Employer
# from main.serializers.position import PositionSelectSerializer

#
# class PermissionSelectSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     codename = serializers.ReadOnlyField()
#
#
# class GroupSelectSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     name = serializers.ReadOnlyField()
#     permissions = PermissionSelectSerializer(many=True)
#
#
# class UserInfoSerializer(serializers.Serializer):
#     position = PositionSelectSerializer()
#     user_type = serializers.ReadOnlyField()
#     groups = GroupSelectSerializer(many=True)
#     username = serializers.ReadOnlyField()
#     id = serializers.SerializerMethodField()
#
#     def get_id(self, obj: User):
#         try:
#             person = getattr(obj, obj.user_type)
#             return person.id
#         except AttributeError:
#             return None
#
#
# class DelegatedAccessCheck(serializers.Serializer):
#     employer = serializers.PrimaryKeyRelatedField(queryset=Employer.objects.all())
#
#     def __init__(self, *args, **kwargs):
#         super(DelegatedAccessCheck, self).__init__(*args, **kwargs)
#         self.request = self.context.get('request')
#         self.user: User = getattr(self.request, 'user', None)
#
#     def validate(self, attrs):
#         errors = defaultdict(list)
#
#         if attrs['employer'].manager != self.user.staff:
#             errors['non_field_errors'].append(
#                 f"You can not get delegated access on employer as you are not manger of {attrs['employer'].title}"
#             )
#
#         if errors:
#             raise serializers.ValidationError(errors)
#         return attrs
from main.serializers.position import GroupSerializer, PermissionSerializer, GroupModelSerializer


class UserCreateModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, required=False, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'groups']

    def validate(self, attrs):
        errors = defaultdict(list)
        users = User.objects.all()
        users = users.filter(username=attrs['username'])

        if self.instance:
            users = users.exclude(pk=self.instance.id)
        if users.exists():
            errors['username'].append('Username has already taken')
        if errors:
            raise serializers.ValidationError(errors)
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super(UserCreateModelSerializer, self).create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super(UserCreateModelSerializer, self).update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def to_representation(self, instance):
        self.fields['groups'] = GroupSerializer(many=True, read_only=True)
        return super(UserCreateModelSerializer, self).to_representation(instance)


class CheckTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
