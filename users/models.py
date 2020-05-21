import uuid

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    confirm_code = models.UUIDField(default=uuid.uuid4(), editable=False)
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.username

