from rest_framework.serializers import ModelSerializer

from mainapp.models import Polling, Question, Answer


class PollSerializer(ModelSerializer):
    """Сериализация формы опроса"""
    class Meta:
        model = Polling
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    """Сериализация формы вопроса"""
    class Meta:
        model = Question
        fields = '__all__'


class AnswerSerializer(ModelSerializer):
    """Сериализация формы ответа"""
    class Meta:
        model = Answer
        fields = '__all__'

