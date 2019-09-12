from core.django.model import BaseModel
from django.db import models


class Question(BaseModel):
    question = models.TextField(blank=True)
    answer = models.TextField(blank=True)

    def __str__(self):
        return self.question
