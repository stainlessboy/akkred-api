from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from main.serializers.questions import QuestionSerializer
from main.models.questions import Question


class QuestionViewSet(viewsets.ModelViewSet):
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    search_fields = ['question', ]
    filter_fields = [
        'question',
    ]
    ordering_fields = ['id', 'create_date']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
