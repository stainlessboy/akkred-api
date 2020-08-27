from main.models.authorized_reestr import AuthorizedReestr
from rest_framework import viewsets, permissions

from main.serializers.authorized_reestr import AuthorizedReestrModelSerializer


class AuthorizedReestrViewSet(viewsets.ModelViewSet):
    model = AuthorizedReestr
    queryset = AuthorizedReestr.objects.all()
    serializer_class = AuthorizedReestrModelSerializer
    ordering_fields = ['id']

    search_fields = ['title_organ',
                     'inn']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super(AuthorizedReestrViewSet, self).get_permissions()
