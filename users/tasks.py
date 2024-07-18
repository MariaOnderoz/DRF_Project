from datetime import timedelta
from django.utils import timezone
from users.models import User


def user_deactivate():
    active_users = User.objects.filter(is_active=True)
    current_date = timezone.now().today().date()

    for user in active_users:
        if user.last_login < (current_date - timedelta(days=30)):
            user.is_active = False
            user.save()
            print(f"Пользователь {user.email} заблоктрован!")


