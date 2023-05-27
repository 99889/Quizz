from django.contrib import admin
from django.urls import include, path
from quizzes import views as quiz_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('quizzes', quiz_views.QuizCreateAPIView.as_view(), name='quiz-create'),
    path('quizzes/active', quiz_views.ActiveQuizRetrieveAPIView.as_view(), name='quiz-active'),
    path('quizzes/<int:id>/result', quiz_views.QuizResultRetrieveAPIView.as_view(), name='quiz-result'),
    path('quizzes/all', quiz_views.QuizListAPIView.as_view(), name='quiz-list'),
]
