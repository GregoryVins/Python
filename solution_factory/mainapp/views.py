from django.utils.timezone import now
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from mainapp.models import Polling, Question, Answer
from mainapp.serializers import PollSerializer, QuestionSerializer, AnswerSerializer


class PollViewSet(ModelViewSet):
    serializer_class = PollSerializer
    queryset = Polling.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return Polling.objects.all()


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]


class ActivePollsViewSet(PollViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        current = []
        for poll in self.queryset:
            if poll.start_time < now() < poll.end_time:
                current.append(poll)

        return self.queryset.filter(title__in=current)


class AnswerViewSet(ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
