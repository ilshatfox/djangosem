import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.db.models import Count, Avg

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vk_bot.settings')
app = Celery('vk_bot')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def info_task(arg):
    from django.core.mail import send_mail
    from users.models import User
    import smtplib

    res = User.objects.annotate(akk_nums=Count('vkakk')).aggregate(Avg('akk_nums'))
    mess = f'Юзеры имеют  в среднем {res["akk_nums__avg"]} аккаунтов'

    try:
        send_mail(subject="Info", message=mess, from_email=settings.DEFAULT_FROM_EMAIL,
                  recipient_list=User.objects.values_list("email", flat=True))
    except smtplib.SMTPException:
        print(f'Не удалось отправить')


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hours=10, minute=50),
        info_task.s("ffff"))