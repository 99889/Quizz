
from __future__ import absolute_import
import os
from celery import Celery
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_app.settings')

app = Celery('quiz_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_app.settings')

app = Celery('quiz_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
