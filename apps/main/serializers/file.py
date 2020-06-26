from easy_thumbnails.files import get_thumbnailer
from rest_framework import serializers

from main.models import File


class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'name', 'content_type']
        extra_kwargs = dict(
            name=dict(read_only=True),
            content_type=dict(read_only=True),
        )

    def create(self, validated_data):
        instance: File = super(FileModelSerializer, self).create(
            validated_data)
        instance.name = instance.file.name
        instance.content_type = instance.name.split('.')[-1]
        instance.save()
        return instance


class FileSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    file = serializers.SerializerMethodField()
    content_type = serializers.ReadOnlyField()

    def __init__(self, *args, **kwargs):
        super(FileSerializer, self).__init__(*args, **kwargs)
        try:
            self.request = self.context['request']
            self.thumbnail_type = self.request.GET.get('thumbnail_type', None)
        except KeyError:
            self.request = None
            self.thumbnail_type = None

    def get_file(self, obj: File):
        if self.thumbnail_type is None:
            url = obj.file.url
        else:
            url = get_thumbnailer(obj.file)[self.size].url

        if self.request:
            return self.request.build_absolute_uri(url)
        return url
