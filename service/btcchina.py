# -*- coding: utf-8 -*-
from entity import beans

flag = "BTCChina"


class BTCChinaBiz(object):
    
    def __init__(self, access_key, secret_key):
        from envoy import btcchina
        self.__envoy = btcchina.BTCChina(access_key, secret_key)

    @staticmethod
    def platform_name():
        return flag

    def get_account(self):
        if self.__envoy is None:
            return None
        btcchina_account = self.__envoy.get_account_info()
        if btcchina_account is not None and btcchina_account['profile'] is not None:
            account = beans.Account()
            account.set_username(btcchina_account['profile']['username'])
            for coinName in btcchina_account['balance']:
                coin = beans.Coin()
                coin_instance = btcchina_account['balance'][coinName]
                coin.set_symbol(coin_instance['symbol'])
                coin.set_currency_code(coin_instance['currency'])
                coin.set_amount(coin_instance['amount'])
                account.balance().append(coin)
            for coinName in btcchina_account['frozen']:
                coin = beans.Coin()
                coin_instance = btcchina_account['frozen'][coinName]
                coin.set_symbol(coin_instance['symbol'])
                coin.set_currency_code(coin_instance['currency'])
                coin.set_amount(coin_instance['amount'])
                account.frozen().append(coin)
            return account
        else:
            return None

    def get_market_depth(self, number=10):
        if self.__envoy is None:
            return None
        btcchina_market_depth = self.__envoy.get_market_depth(limit=number)
        if btcchina_market_depth is not None:
            btcchina_market_depth['ask'].reverse()
            result = beans.MarketDepth()
            for btcchina_bid in btcchina_market_depth['bid']:
                bid = beans.Offer()
                bid.set_price(btcchina_bid['price'])
                bid.set_volume(btcchina_bid['amount'])
                result.bids().append(bid)
            for btcchina_ask in btcchina_market_depth['ask']:
                ask = beans.Offer()
                ask.set_price(btcchina_ask['price'])
                ask.set_volume(btcchina_ask['amount'])
                result.asks().append(ask)
            return result
        else:
            return None
            
    def order(self, price=0.0, amount=0.0, buy1sell0=1):
        if self.__envoy is None:
            return None
        if buy1sell0 == 1:
            return self.__envoy.buy_order(price, amount)
        if buy1sell0 == 0:
            return self.__envoy.sell_order(price, amount)
        else:
            return None

    def cancel(self, order):
        if self.__envoy is None:
            return None
        return self.__envoy.cancel_order(order.order_id())

    def get_orders(self):
        if self.__envoy is None:
            return None
        btcchina_orders = self.__envoy.get_orders(open_only=False)
        if btcchina_orders is not None and btcchina_orders['order'] is not None:
            orders = beans.Orders()
            for btcchina_order in btcchina_orders['order']:
                order = beans.Order()
                order.set_order_id(btcchina_order['id'])
                order.set_amount(float(btcchina_order['amount']))
                order.set_price(float(btcchina_order['price']))
                status_str = btcchina_order['status']
                status_str = status_str[0].upper() + status_str[1:]
                order.set_status(status_str)
                order.set_date_time(btcchina_order['date'])
                order.set_type('BUY' if btcchina_order['type'] == 'bid' else ('SELL' if btcchina_order['type'] == 'ask' else 'NoType'))
                orders.buy_orders().append(order) if order.type() == 'BUY' else orders.sell_orders().append(order)
            return orders

newInstance = BTCChinaBiz
