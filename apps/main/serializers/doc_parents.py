from rest_framework import serializers
from main.models.documens_parent import DocParent
from main.models.documents_type import DocType


class DocumentSelectListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()


class DocParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocParent
        fields = '__all__'


class DocTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocType
        fields = '__all__'
