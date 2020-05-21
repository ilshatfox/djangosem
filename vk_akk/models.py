from django.db import models

# Create your models here.
from django.db.models import ManyToManyField

from proxies.models import Proxy
from users.models import User


class UserAgent(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user_agent = models.TextField(unique=True)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.__dict__)

    __repr__ = __str__


class VkAkk(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    login = models.TextField(unique=True)
    password = models.TextField()
    vk_user_id = models.TextField(default='-1')
    proxy = models.ForeignKey(Proxy, on_delete=models.DO_NOTHING, null=True)
    _cookies = models.TextField(default='{}')
    user_agent = models.ForeignKey(UserAgent, on_delete=models.DO_NOTHING, null=True)
    is_auth = models.BooleanField(default=False)
    is_ban = models.BooleanField(default=False)
    vk_url = models.URLField(null=True)
    vk_last_auth_time = models.DateTimeField(auto_now=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # return '{}({})'.format(self.__class__.__name__, self.__dict__)
        return '{}'.format(self.__class__.__name__)
    __repr__ = __str__

    def get_cookies(self):
        return eval(self._cookies)

    def set_cookies(self, cookies: str):
        self._cookies = cookies

    def get_default_headers(self):
        headers = {'User-Agent': self.user_agent.user_agent,
                   'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4',
                   'Connection': 'keep-alive',
                   'Accept-Encoding': 'gzip, deflate'}
        return headers


class VkAkksGroup(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.TextField(unique=True, db_index=True)
    vk_akks = ManyToManyField(VkAkk)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def get_akks_size(self):
        return len(VkAkk.objects.filter(vkakksgroup=self))

    def __str__(self):
        # self.__dict__.update({'group_size': len(list(self.vk_akks.all()))})
        # return '{}({})'.format(self.__class__.__name__, self.__dict__)
        return '{}'.format(self.__class__.__name__)

    __repr__ = __str__
