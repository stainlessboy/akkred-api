from rest_framework import serializers
from main.models.documents import Document, CategoryDocumentForm


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
    document_forms = DocumentFormSerializer(required=False, many=True,)
    forms = serializers.SerializerMethodField(required=False)

    # TODO: 11 Для инспекционных органов
    # TODO: 3 Для провайдеров программ проверки квалификации
    # TODO: 1 Для лабораторий
    class Meta:
        model = Document
        exclude = ['created_date']

    def to_representation(self, instance):
        self.fields['parents'] = DocumentParentSerializer()
        self.fields['type'] = DocumentTypeSerializer()
        return super(DocumentSerializer, self).to_representation(instance)

    def get_forms(self, obj: Document):
        response = list()

        categories = CategoryDocumentForm.objects.all()
        all_forms = obj.document_forms.all()
        for category in categories:
            forms = all_forms.filter(category=category.id)
            if forms:
                form_list = list()
                for form in forms:
                    form_list.append(dict(
                        id=form.id,
                        title=form.title,
                        title_ru=form.title_ru,
                        title_uz=form.title_uz,
                        category=form.category.id,
                        file=str(
                            'http://akkred.uz:8081/media/' + str(form.file)),
                    ))

                response.append(
                    dict(
                        category=dict(
                            id=category.id,
                            title=category.title,
                            title_ru=category.title_ru,
                            title_uz=category.title_uz,
                        ),
                        childrens=form_list
                    )

                )
        return response
