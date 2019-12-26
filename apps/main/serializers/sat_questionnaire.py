from rest_framework import serializers
from main.models.satisfaction_questionnaire import SatisfactionQuestionnaire


class SatisfactionQuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = SatisfactionQuestionnaire
        fields = '__all__'