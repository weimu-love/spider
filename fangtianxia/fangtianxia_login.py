# -*- coding: utf-8 -*-
"""
   File Name：     fangtianxia_login
   Description :
   date：          2020/2/21
"""
import requests
import execjs

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Referer': 'https://passport.fang.com/'
}


class FangJS(object):
    def __init__(self, username=None, password=None):
        self.url = 'https://passport.fang.com/'
        self.login_url = 'https://passport.fang.com/login.api'
        self.username = username
        self.password = password
        self.ctx = None
        self.data = {
            'Service': 'soufun-passport-web',
            'AutoLogin': '1',
            'uid': self.username
        }

    def get_pwd(self):
        if self.ctx is None:
            with open('fangtianxia.js', 'r', encoding='utf-8') as f:
                self.ctx = execjs.compile(f.read())
        pwd = self.ctx.call('getPwd', self.password)
        print(pwd)
        self.data['pwd'] = pwd

    def login(self):
        resp = requests.post(self.login_url, headers=HEADERS, data=self.data)
        print(resp.json())


if __name__ == '__main__':
    fang_js = FangJS('username', 'password')
    fang_js.get_pwd()
    print(fang_js.data)
    fang_js.login()
