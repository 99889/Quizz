from django.db import models

class Quiz(models.Model):
    question = models.CharField(max_length=255)
    options = models.JSONField()
    right_answer = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, default='inactive')

    def __str__(self):
        return self.question
