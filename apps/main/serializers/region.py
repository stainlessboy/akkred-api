from main.models.region import Region
from rest_framework import serializers
from collections import defaultdict


class RegionSelectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()


class RegionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        exclude = ['modified_date']
