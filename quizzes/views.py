from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Quiz
from .serializers import QuizSerializer

class QuizCreateAPIView(generics.CreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class ActiveQuizRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Quiz.objects.filter(status='active')
    serializer_class = QuizSerializer

class QuizResultRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        quiz_id = self.kwargs['id']
        return Quiz.objects.filter(id=quiz_id, status='finished')

class QuizListAPIView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
