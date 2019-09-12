from django.contrib.auth.models import Group, Permission
from rest_framework import permissions, status, mixins
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from core.rest_framework.permissions import IsAuthenticated
from main.models import User
from main.serializers.position import GroupModelSerializer, PermissionSerializer
from main.serializers.user import CheckTokenSerializer, UserCreateModelSerializer


class UserViewSet(GenericViewSet):
    serializer_class = AuthTokenSerializer
    queryset = User.objects.all()

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def login(self, request: Request):
        self.serializer_class = AuthTokenSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    @action(['DELETE'], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request: Request):
        Token.objects.get(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(['GET'], detail=False, url_path='check_token/(?P<token>.{40})', permission_classes=[permissions.AllowAny])
    def check_token(self, request, token=None):
        serializer = CheckTokenSerializer(data=dict(token=token))
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['token']
        token = Token.objects.filter(key=token).first()
        if token:
            user_type, person = token.user.person
            serializer = {
            }.get(user_type, None)
            if serializer:
                data = serializer(person).data
            else:
                data = dict(username=person.username)
            perm_serializer = GroupModelSerializer(token.user.groups.all(), many=True)
            data = dict(
                user=data,
                is_superuser=token.user.is_superuser,
                groups=perm_serializer.data
            )
            return Response(data)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ManagerViewSet(ModelViewSet):
    """
            retrieve:
            Return object of Manager

            list:
            Return a list of Managers objects

            create:
            Create a new  instance of Managers
            ###Request body

                {

                    'password': 'current_password_123',                     # password
                    'username': 'wienerdeming'                              # username
                    'groups': []
                }

            update:
            Update fields of Employers object
        """
    serializer_class = UserCreateModelSerializer
    queryset = User.objects.all()


class GroupViewSet(ModelViewSet):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    search_fields = ['name']


class PermissionViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    search_fields = ['name']
