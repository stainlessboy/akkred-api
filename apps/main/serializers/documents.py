from rest_framework import serializers
from main.models.documents import Document


class DocumentParentSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()
    name_en = serializers.ReadOnlyField()
    name_ru = serializers.ReadOnlyField()
    name_uz = serializers.ReadOnlyField()


class DocumentTypeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()
    name_en = serializers.ReadOnlyField()
    name_ru = serializers.ReadOnlyField()
    name_uz = serializers.ReadOnlyField()


class DocumentFormSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.ReadOnlyField()
    file = serializers.FileField()

    def to_representation(self, instance):
        self.fields['category'] = DocumentTypeSerializer()
        return super(DocumentFormSerializer, self).to_representation(instance)


class DocumentSerializer(serializers.ModelSerializer):
    document_forms = DocumentFormSerializer(required=False, many=True)

    class Meta:
        model = Document
        exclude = ['created_date']

    def to_representation(self, instance):
        self.fields['parents'] = DocumentParentSerializer()
        self.fields['type'] = DocumentTypeSerializer()
        return super(DocumentSerializer, self).to_representation(instance)
