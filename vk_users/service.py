from django.db.transaction import atomic

from vk_bot.base.status import Status
from vk_users.models import VkUsersGroup, VkUser, VkFileUsers
from django.db import connection


def add_users_group(user_ids, group_name, user):
    ids = [int(user_id) for user_id in user_ids]
    users = list(create_much_users(ids))
    users = VkUser.objects.in_bulk(ids, field_name='vk_id').values()
    # print('ids', ids)
    # print(users)
    # print(connection.queries)
    group = VkUsersGroup.objects.get_or_create(name=group_name, user=user)
    group = VkUsersGroup.objects.get(name=group_name, user=user)
    group.save()
    for user in users:
        # print(user.id)
        group.users.add(user)
    group.save()
    return [Status(True, "Успешно добавил аудиторию!")]


@atomic
def create_much_users(user_ids):
    objs = []
    for user_id in user_ids:
        obj = VkUser.objects.get_or_create(vk_id=user_id)
        obj = obj[0]
        # print(obj)
        # obj.save()
        objs.append(obj)
    return list(objs)

#
# @atomic
# def get_users(user_ids):
#     VkUsersGroup.objects.in_bulk()


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def save_user_file(file, user):
    VkFileUsers.objects.create(file=file, user=user)