import os

from django.core.files.base import ContentFile
from django.db import models

# Create your models here.
from django.db.models import ManyToManyField

from users.models import User
from vk_bot import settings


class VkUser(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    vk_id = models.IntegerField(unique=True, db_index=True)
    vk_username = models.TextField(default='')

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.__dict__)

    __repr__ = __str__


class VkUsersGroup(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.TextField(unique=True, db_index=True)
    users = ManyToManyField(VkUser)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def users_size(self):
        return len(VkUser.objects.filter(vkusersgroup=self))

    def __str__(self):
        self.__dict__.update({'group_size': len(list(self.users.all()))})
        return '{}({})'.format(self.__class__.__name__, self.__dict__)

    __repr__ = __str__


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'documents/user_{}/{}'.format(instance.user.id, instance.filename)
    # from django.core.files.storage import default_storage


class VkFileUsers(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    filename = models.TextField(default='fff')
    file = models.FileField(upload_to=user_directory_path)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def write_file(cls, filename, file, user):
        path = 'documents/user_{}/{}'.format(user.id, filename)

        obj = VkFileUsers.objects.create(filename=filename, file=file, user=user)


class VkNews(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.TextField()
    body = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
