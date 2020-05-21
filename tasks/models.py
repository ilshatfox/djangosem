from django.db import models

# Create your models here.
from tasks.enums import TaskType, FollowTaskStatusType
from users.models import User
from vk_akk.models import VkAkk, VkAkksGroup
from vk_users.models import VkUser, VkUsersGroup


class FollowTask(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    vk_akks_group = models.ForeignKey(VkAkksGroup, on_delete=models.CASCADE)
    vk_users_group = models.ForeignKey(VkUsersGroup, on_delete=models.CASCADE)
    # task_type = models.TextField(choices=TaskType.choices())
    follow_number = models.IntegerField()
    status = models.TextField(choices=FollowTaskStatusType.choices(), default=FollowTaskStatusType.NEW)
    is_fast_follow = models.BooleanField(default=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return '{}({})'.format(self.__class__.__name__, self.__dict__)
        return '{}'.format(self.__class__.__name__)
    __repr__ = __str__


class AkkFollowTask(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    vk_akk = models.ForeignKey(VkAkk, on_delete=models.CASCADE)
    vk_users = models.ManyToManyField(VkUser)
    complete_num = models.IntegerField(default=0)
    success_num = models.IntegerField(default=0)

    follow_task = models.ForeignKey(FollowTask, on_delete=models.CASCADE)

    def __str__(self):
        # self.__dict__.update({'users_size': len(list(self.vk_users.all()))})
        return '{}'.format(self.__class__.__name__)

    __repr__ = __str__

# class VkAkkSelfTask(models.Model):
#     pass
#
#
# class EditStatusTask(models.Model):
#     pass
#
#
# class DeletePostTask(models.Model):
#     pass
