import smtplib

from django.core.mail import send_mail
from django.db.models import Count, Avg
from django.template.loader import render_to_string

from users.models import User
from vk_akk.models import VkAkk
from vk_bot import settings
from vk_bot.celery import app


@app.task
def send_email(subject, from_email, to_email, template, args):

    html_message = render_to_string(template, args)
    try:
        print('fff')
        res = send_mail(subject=subject, message='', from_email=from_email,
                  recipient_list=[to_email], html_message=html_message)
        print(res)
    except smtplib.SMPTException:
        print(f'Error while sending email to {to_email}')

