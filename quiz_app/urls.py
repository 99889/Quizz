from django.urls import path
from quizzes.views import (
    QuizCreateAPIView,
    ActiveQuizRetrieveAPIView,
    QuizResultRetrieveAPIView,
    QuizListAPIView,
)
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('quizzes.urls')),
]


urlpatterns = [
    path('quizzes', QuizCreateAPIView.as_view(), name='quiz-create'),
    path('quizzes/active', ActiveQuizRetrieveAPIView.as_view(), name='quiz-active'),
    path('quizzes/<int:id>/result', QuizResultRetrieveAPIView.as_view(), name='quiz-result'),
    path('quizzes/all', QuizListAPIView.as_view(), name='quiz-list'),
]
