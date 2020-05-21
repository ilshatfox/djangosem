from celery.schedules import crontab
from vk_bot.celery import app
from users.tasks import info_task

