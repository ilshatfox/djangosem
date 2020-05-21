import re
import traceback

from proxies.models import Proxy
from vk_akk.models import VkAkk, UserAgent, VkAkksGroup
from vk_api_module.vk_api import VkApi
from vk_bot.base.status import Status
from vk_users.models import VkUser


def get_my_vk_akks(user):
    akks = VkAkk.objects.filter(user=user)
    return akks


def auth_vk_akk(user, akk_id):
    akk = get_my_vk_akks(user).filter(id=int(akk_id)).first()
    if akk:
        auth_akk(akk)


def auth_akk(akk: VkAkk):
    print(akk)
    api = VkApi(akk)
    api.check_and_auth()
    user = VkUser.objects.filter(vk_id=int('222031326')).first()
    api.add_friend(user)
    input('ffff')


def add_akks(akk_lines, user):
    results = []
    for line in akk_lines:
        try:
            split_line = re.split(r'\s+', line)
            akk, proxy, user_w = split_line[0], split_line[1], split_line[2]
            user_agent = line[str(line).index(user_w):]
            print(akk, proxy, user_agent)
            akk_log_pass = akk.split(':')
            proxy = Proxy.find_proxy(proxy)
            user_agent = UserAgent.objects.filter(user_agent=user_agent).first()
            print(proxy)
            print(user_agent)
            if proxy and user_agent:
                VkAkk.objects.create(login=akk_log_pass[0], password=akk_log_pass[1], proxy=proxy,
                                     user_agent=user_agent, user=user)
                results.append(Status(True, "Успешно добавил аккаунт"))
            else:
                results.append(Status(False, "Не удалось добавить аккаунт proxy или user_agent не найден"))
        except:
            print(traceback.format_exc())
            results.append(Status(False, "Не удалось добавить аккаунт"))
    return results


def add_akks_group(akk_logins, group_name, user):
    print('akk_logins', akk_logins)
    akks = VkAkk.objects.in_bulk(akk_logins, field_name='login')
    print('akks', akks)
    vk_akk_group = VkAkksGroup.objects.get_or_create(name=group_name, user=user)
    vk_akk_group = VkAkksGroup.objects.get(name=group_name)
    for akk in akks.values():
        vk_akk_group.vk_akks.add(akk)
    vk_akk_group.save()
