from rest_framework import serializers
from main.models.review import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['created_date']
