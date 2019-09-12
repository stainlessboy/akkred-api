from rest_framework import serializers
from main.models.media import Media


class MediaSerializers(serializers.Serializer):
    class Meta:
        model = Media
        exclude = ['modified_date']

