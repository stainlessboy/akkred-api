from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from main.serializers.sat_questionnaire import SatisfactionQuestionnaireSerializer
from main.models.satisfaction_questionnaire import SatisfactionQuestionnaire


class SatisfactionQuestionnaireViewSet(viewsets.ModelViewSet):
    model = SatisfactionQuestionnaire
    queryset = SatisfactionQuestionnaire.objects.all()
    serializer_class = SatisfactionQuestionnaireSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [AllowAny()]
        return super().get_permissions()
