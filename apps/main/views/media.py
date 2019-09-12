from main.serializers.media import MediaSerializers
from main.models.media import Media
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class MediaViewSet(viewsets.ModelViewSet):
    model = Media
    queryset = Media.objects.all()
    serializer_class = MediaSerializers
    search_fields = ['title', 'description']
    filter_fields = [
        'title',
    ]
    ordering_fields = ['id', 'create_date']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
