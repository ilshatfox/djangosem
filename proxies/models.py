from django.db import models

# Create your models here.
from proxies.enums import ProxyType
from users.models import User


class Proxy(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    ip = models.CharField(unique=True, max_length=255)
    port = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    type = models.CharField(choices=ProxyType.choices(), max_length=255)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.__class__.__name__)

    __repr__ = __str__

    def get_dict_proxy(self):
        proxy = 'http://{}:{}@{}:{}'.format(self.login, self.password, self.ip, self.port)
        proxies = {'http': proxy,
                   'https': proxy.replace('http', 'https')}
        return proxies

    @staticmethod
    def find_proxy(proxy_line):
        try:
            ip, port, login, password, pr_type = proxy_line.split(':')
            obj = Proxy.objects.filter(ip=ip, port=port, login=login, password=password).first()
            return obj
        except:
            return False
