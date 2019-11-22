
from main.models.reestr_info_user import ReestrInfoUser
from rest_framework import viewsets, permissions
from main.serializers.reestr_info import ReestrInfoUserSerializer


class ReestrInfoUserViewSet(viewsets.ModelViewSet):
    model = ReestrInfoUser
    queryset = ReestrInfoUser.objects.all()
    serializer_class = ReestrInfoUserSerializer
    ordering_fields = ['id', 'create_date']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super(ReestrInfoUserViewSet, self).get_permissions()

