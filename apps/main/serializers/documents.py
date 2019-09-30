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


# class DocumentsSelectSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     title = serializers.ReadOnlyField()
#
#
# class DocuemtnsListSerializer(serializers.Serializer):
#     parents = serializers.SerializerMethodField()
#     count = serializers.ReadOnlyField()
#
#     # documents = serializers.SerializerMethodField()
#
#     def get_parents(self, obj):
#         childs_list = list()
#         childs = Document.objects.filter(parents=obj['parents_id'])
#         print(childs)
#         for child in childs:
#             childs_list.append(dict(id=child.id, title=child.title))
#
#         print(childs_list)
#         # print(dict(id=obj['parents_id'], title=obj['parents__title'],values = childs_list))
#         return dict(id=obj['parents_id'], title=obj['parents__title'],
#                     values=childs_list)
#         # return dict(id=obj['parents_id'], title=obj['parents__title'],values =news_child)
