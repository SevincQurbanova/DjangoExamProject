# djangoexamapp/tasks.py
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Employee

@shared_task
def notify_inactive_users():
    two_days_ago = timezone.now() - timedelta(days=2)
    inactive_users = Employee.objects.filter(created_at__lt=two_days_ago, status='inactive')
    for user in inactive_users:
        # Logic to send notification (e.g., email)
        print(f'Notifying {user.name} {user.surname} (ID: {user.id})')
