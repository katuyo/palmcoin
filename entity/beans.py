# -*- coding: utf-8 -*-


class Offer(object):

    def __init__(self):
        self.__price = 0.0
        self.__volume = 0.0
    
    def price(self):
        return self.__price
    
    def volume(self):
        return self.__volume
    
    def set_price(self, price):
        self.__price = price
    
    def set_volume(self, volume):
        self.__volume = volume


class MarketDepth(object):
    
    def __init__(self):
        self.__bids = []
        self.__asks = []

    def bids(self):
        return self.__bids
    
    def asks(self):
        return self.__asks
    
    def set_bids(self, bids):
        self.__bids = bids
    
    def set_asks(self, asks):
        self.__asks = asks


class Coin(object):
    
    def __init__(self):
        self.__currencyCode = ''
        self.__symbol = ''
        self.__amount = 0.0
        
    def currency_code(self):
        return self.__currencyCode
    
    def set_currency_code(self, currency_code):
        self.__currencyCode = currency_code
        
    def symbol(self):
        return self.__symbol
    
    def set_symbol(self, symbol):
        self.__symbol = symbol
    
    def amount(self):
        return self.__amount
    
    def set_amount(self, amount):
        self.__amount = amount


class Account(object):
    
    def __init__(self):
        self.__username = ''
        self.__balance = []
        self.__frozen = []
    
    def username(self):
        return self.__username
    
    def set_username(self, username):
        self.__username = username
    
    def balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance
    
    def frozen(self):
        return self.__frozen
    
    def set_frozen(self, frozen):
        self.__frozen = frozen


class Order(object):
    
    def __init__(self):
        self.__order_id = '0'
        self.__type = 'BUY'
        self.__currency_pair = 'BTC/CNY'
        self.__price = 0.0
        self.__amount = 0.0
        self.__date_time = 0
        self.__status = 'closed'

    def order_id(self):
        return self.__order_id

    def price(self):
        return self.__price
    
    def amount(self):
        return self.__amount

    def type(self):
        return self.__type

    def currency_pair(self):
        return self.__currency_pair

    def date_time(self):
        return self.__date_time

    def status(self):
        return self.__status

    def set_order_id(self, order_id):
        self.__order_id = order_id

    def set_price(self, price):
        self.__price = price
    
    def set_amount(self, amount):
        self.__amount = amount

    def set_type(self, order_type):
        self.__type = order_type

    def set_currency_pair(self, currency_pair):
        self.__currency_pair = currency_pair

    def set_date_time(self, date_time):
        self.__date_time = date_time

    def set_status(self, status):
        self.__status = status


class Orders(object):
    def __init__(self):
        self.__buy_orders = []
        self.__sell_orders = []

    def buy_orders(self):
        return self.__buy_orders

    def sell_orders(self):
        return self.__sell_orders

    def set_buy_orders(self, buy_orders):
        self.__buy_orders = buy_orders

    def set_sell_orders(self, sell_orders):
        self.__sell_orders = sell_orders