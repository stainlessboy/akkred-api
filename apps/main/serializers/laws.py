from rest_framework import serializers

from main.models import Laws, LawsCategory


class LawsCategorySelectSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()


class LawsModelSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=LawsCategory.objects.all())

    class Meta:
        model = Laws
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['category'] = LawsCategorySelectSerializers()
        return super().to_representation(instance)


class LawsCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LawsCategory
        fields = '__all__'
