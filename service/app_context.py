# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
__author__ = 'Palm Tale'

from service import btcchina


class AppContext(object):
    SINGLE = None
    __platforms__ = {'BTCChina': btcchina.BTCChinaBiz}

    def __init__(self):
        self.__platformBiz = None
        self.__account = None
        return None

    def set_platform_biz(self, platform_biz):
        self.__platformBiz = platform_biz
        
    def platform_biz(self):
        return self.__platformBiz
        
    def set_account(self, account):
        self.__account = account
        
    def current_account(self):
        return self.__account

    @staticmethod
    def validate_account(platform_name, access_key, secret_key):
        platform_biz = AppContext.__platforms__[platform_name](access_key, secret_key)
        account = platform_biz.get_account()
        if account is not None:
            get.set_platform_biz(platform_biz)
            get.set_account(account)
            return True
        else:
            return False

if AppContext.SINGLE is None:
    AppContext.SINGLE = AppContext()
get = AppContext.SINGLE
