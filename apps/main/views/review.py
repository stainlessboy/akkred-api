from rest_framework.pagination import PageNumberPagination

from main.serializers.review import ReviewSerializer
from main.models.review import Review
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ReviewViewSet(viewsets.ModelViewSet):
    model = Review
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    search_fields = ['author', 'description']
    filter_fields = ['author', 'description']
    ordering_fields = ['id', 'created_date']
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
