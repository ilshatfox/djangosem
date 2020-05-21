import random
import threading
import time
from typing import List

from tasks.models import AkkFollowTask
from vk_api_module.vk_api import VkApi
from vk_users.models import VkUser


def start_follow_tasks(vk_follow_tasks: List[AkkFollowTask]):
    for task in vk_follow_tasks:
        thread = threading.Thread(target=start_follow_task, args=(task,))
        thread.setDaemon(True)
        thread.start()


def start_follow_task(vk_follow_task: AkkFollowTask):
    vk_api = VkApi(vk_follow_task.vk_akk)
    vk_users = VkUser.objects.filter(akkfollowtask=vk_follow_task)
    for user in vk_users:
        res = vk_api.add_friend(user.vk_id)
        if res:
            vk_follow_task.success_num += 1
        vk_follow_task.complete_num += 1
        vk_follow_task.save()
        time.sleep(40 + random.randrange(40))