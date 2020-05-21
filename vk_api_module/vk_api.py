# Здесь будет апи вк
# Не ебись с селери сначала, сделать тупо в потоках!
import re
import time
import traceback

import requests

from vk_akk.models import VkAkk
from vk_users.models import VkUser


class VkApi:
    def __init__(self, akk_obj: VkAkk):
        self.akk_obj = akk_obj
        self.s = requests.session()
        self.update_session()
        self.update_proxy()

    def update_session(self):
        self.s.cookies.update(self.akk_obj.get_cookies())

    def update_proxy(self):
        self.s.proxies = self.akk_obj.proxy.get_dict_proxy()

    def auth(self):
        try:
            req = self.s.get('https://m.vk.com/login')
            data = {}
            url = re.findall('https://login\.vk\.com/\?act=login[^"]*', req.text)[0]
            print(url)
            data['email'] = str(self.akk_obj.login)
            data['pass'] = str(self.akk_obj.password)
            time.sleep(1)
            req = self.s.post(url, data=data)
            print(req.text)
            time.sleep(1)
            check = self.check_auth()
            print('check', check)
            self.akk_obj.is_auth = check
            self.akk_obj.set_cookies(str(self.s.cookies.get_dict()))
            self.akk_obj.save()
            self.update_my_akk_id()
        except:
            print(traceback.format_exc())
            pass

    def check_auth(self):
        url = 'https://m.vk.com/'
        req = self.s.get(url)
        if 'href="/settings?act=menu"' in str(req.text):
            return True
        else:
            return False

    def check_and_auth(self):
        if not self.check_auth():
            return self.auth()
        self.update_my_akk_id()
        return False

    def follow(self, vk_user: VkUser):
        pass

    def get_my_akk_id(self):
        try:
            url = 'https://m.vk.com/settings?act=change_addr'
            req = self.s.get(url)
            # print(req.text)
            akk_id = re.findall(r'"id\d+"', req.text)[0]
            # print('akk_id', akk_id)
            return akk_id[3:-1]
        except:
            return False

    def update_my_akk_id(self):
        time.sleep(1)
        akk_id = self.get_my_akk_id()
        if akk_id:
            self.akk_obj.vk_user_id = akk_id
            self.akk_obj.vk_url = 'https://m.vk.com/id{}'.format(akk_id)
            self.akk_obj.save()

    def add_friend(self, vk_user: VkUser):
        url = 'https://m.vk.com/id{}'.format(vk_user.vk_id)
        req = self.s.get(url)
        urls = re.findall(r'/friends\?act=accept[^"]*', req.text)
        print(urls)
        url = urls[0]
        if url:
            url = url.replace('amp;', '')
            self.work = self.s.post('https://m.vk.com' + url)
            return True, url
        else:
            print('Заявка уже отправлена')
            return True, 'true'
