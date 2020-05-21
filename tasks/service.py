from tasks.enums import FollowTaskStatusType
from tasks.models import FollowTask, AkkFollowTask
from vk_akk.models import VkAkksGroup, VkAkk
from vk_users.models import VkUsersGroup, VkUser


def create_follow_task(vk_akks_group_id: int, vk_users_group_id: int, follow_number: int, user):
    vk_akks_group = VkAkksGroup.objects.get(id=vk_akks_group_id)
    vk_users_group = VkUsersGroup.objects.get(id=vk_users_group_id)
    print(vk_akks_group)
    print(vk_users_group)
    FollowTask.objects.create(vk_akks_group=vk_akks_group, vk_users_group=vk_users_group, follow_number=follow_number, user=user)


def start_follow_task_with_id(follow_task_id):
    follow_task = FollowTask.objects.filter(id=follow_task_id).first()
    if follow_task:
        start_follow_task(follow_task)


def start_follow_task(follow_task: FollowTask):
    akk_follow_tasks = create_akk_follow_tasks(follow_task)
    # запускать


def create_akk_follow_tasks(follow_task: FollowTask):
    if follow_task.status == FollowTaskStatusType.NEW:
        akks = VkAkk.objects.filter(vkakksgroup__followtask=follow_task)
        print(akks)
        users = list(VkUser.objects.filter(vkusersgroup__followtask=follow_task))
        print(users)
        follow_num = follow_task.follow_number
        min_follow_num = int(len(users) / len(akks))
        users_groups = []
        for user_group in range(int(len(users) / min_follow_num)):
            group = users[user_group * min_follow_num: (user_group + 1) * min_follow_num][:follow_num]
            users_groups.append(group)

        akk_follow_tasks = []
        for i in range(len(akks)):
            obj = AkkFollowTask.objects.create(vk_akk=akks[i], follow_task=follow_task)
            obj = AkkFollowTask.objects.get(vk_akk=akks[i], follow_task=follow_task)
            vk_users = users_groups[i]
            for user in vk_users:
                obj.vk_users.add(user)
            obj.save()
            akk_follow_tasks.append(obj)

        follow_task.status = FollowTaskStatusType.READY_TO_START
        follow_task.save()
        return akk_follow_tasks
    else:
        return AkkFollowTask.objects.filter(follow_task=follow_task)
