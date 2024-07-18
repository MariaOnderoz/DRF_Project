from django.core.mail import send_mail
from celery import shared_task
from config import settings
from materials.models import Course, Subscription


@shared_task
def send_email(course_id):
    course = Course.objects.get(id=course_id)
    subscribers = Subscription.objects.filter(course=course)

    send_mail(
        subject=f"Обновление курса {course}",
        message=f"Курс {course} был обновлен",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[subscribers.user.email],
    )



