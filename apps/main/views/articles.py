from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from main.models.articles import Articles
from main.serializers.articles import ArticlesSerializer


class ArticlesViewSet(viewsets.ModelViewSet):
    model = Articles
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    filter_fields = ['title', ]
    search_fields = ['title', 'description']
    ordering_fields = ['id', 'create_date']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
