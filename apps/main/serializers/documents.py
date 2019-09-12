from rest_framework import serializers
from main.models.documents import Document
from main.serializers.file import FileSerializer


class DocumentParentSerializer(serializers.Serializer):
    title = serializers.ReadOnlyField()


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        exclude = ['created_date']

    def to_representation(self, instance):
        self.fields['file'] = FileSerializer(context=self.context)
        self.fields['parents'] = DocumentParentSerializer()
        return super(DocumentSerializer, self).to_representation(instance)
