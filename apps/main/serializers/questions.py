from rest_framework import serializers
from main.models.questions import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        exclude = ['created_date']
