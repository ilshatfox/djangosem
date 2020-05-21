from django.db.models import Q

from proxies.models import Proxy
from vk_bot.base.status import Status


def add_proxies(proxy_lines, user):
    results = []
    for proxy in proxy_lines:

        try:
            ip, port, login, password, pr_type = proxy.split(':')
            # if pr_type not in
            Proxy.objects.create(
                Q(ip=ip) & Q(port=port) & Q(login=login) & Q(password=password) & Q(type=pr_type) & Q(user=user))

            results.append(Status(True, "Успешно добавил: {}".format(proxy)))
        except:
            results.append(Status(False, "Не удалось добавить: {}".format(proxy)))
    return results
