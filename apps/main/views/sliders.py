from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from main.serializers.sliders import SliderSerializer
from main.models.sliders import Slider


class SliderViewSet(viewsets.ModelViewSet):
    model = Slider
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    search_fields = ['title']
    filter_fields = ['title']
    ordering_fields = ['id', 'created_date']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
