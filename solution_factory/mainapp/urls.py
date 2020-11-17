from rest_framework.routers import DefaultRouter

from mainapp.views import PollViewSet, QuestionViewSet, ActivePollsViewSet, AnswerViewSet

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')
router.register('quest', QuestionViewSet, basename='quest')
router.register('active', ActivePollsViewSet, basename='active')
router.register('answer', AnswerViewSet, basename='answer')

urlpatterns = router.urls
