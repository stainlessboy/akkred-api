from rest_framework import serializers

from main.models import News
from main.serializers.file import FileSerializer


class NewsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        extra_kwargs = dict(
            gallery=dict(required=False),
            text=dict(required=False),
            title=dict(required=False),
            photo=dict(required=False),

        )

    def to_representation(self, instance):
        self.fields['photo'] = FileSerializer(context=self.context)
        # self.fields['gallery'] = FileSerializer(context=self.context)
        self.fields['gallery'] = FileSerializer(context=self.context, required=False, many=True)
        return super().to_representation(instance)
