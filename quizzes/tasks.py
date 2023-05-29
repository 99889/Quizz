from celery import shared_task
from django.utils import timezone
from .models import Quiz

@shared_task
def update_quiz_status():
    current_time = timezone.now()
    active_quizzes = Quiz.objects.filter(start_date__lte=current_time, end_date__gte=current_time)
    inactive_quizzes = Quiz.objects.filter(start_date__gt=current_time)

    active_quizzes.update(status='active')
    inactive_quizzes.update(status='inactive')
