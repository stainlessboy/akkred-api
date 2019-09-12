from rest_framework import serializers
from main.models.documens_parent import DocParent


class DocParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocParent
        fields = '__all__'


