from rest_framework import serializers
from main.models.documens_parent import DocParent


class DocumentSelectListSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()


class DocParentSerializer(serializers.ModelSerializer):
    # documents = DocumentSelectListSerializer(many=True, required=False)

    class Meta:
        model = DocParent
        fields = '__all__'
