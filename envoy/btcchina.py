# -*- coding: utf-8 -*-

import time
import re
import hmac
import hashlib
import base64
import httplib2
import json


class BTCChina():

    def __init__(self, access_key=None, secret_key=None):
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.__url = "https://api.btcchina.com/api_trade_v1.php"
        self.__http_client = httplib2.Http(ca_certs="cacert.pem")
        self.__encoding = "utf8"
    
    def __str_bytes(self, string):
        return bytes(string, encoding=self.__encoding)
    
    def __bytes_str(self, byte_array):
        return str(byte_array, encoding=self.__encoding)
 
    def _get_params_hash(self, p_dict):
        p_string = ""
        # The order of params is critical for calculating a correct hash
        fields = ['tonce', 'accesskey', 'requestmethod', 'id', 'method', 'params']
        for f in fields:
            if p_dict[f]:
                if f == 'params':
                    # Convert list to string, then strip brackets and spaces
                    # probably a cleaner way to do this
                    param_string = re.sub("[\[\] ]", "", str(p_dict[f]))
                    param_string = re.sub("'", '', param_string)
                    param_string = re.sub("True", '1', param_string)
                    param_string = re.sub("False", '', param_string)                    
                    p_string += f+'='+param_string+'&'
                else:
                    p_string += f+'='+str(p_dict[f])+'&'
            else:
                p_string += f+'=&'
        p_string = p_string.strip('&')
        
        # now with correctly ordered param string, calculate hash
        p_hash = hmac.new(self.__str_bytes(self.__secret_key), self.__str_bytes(p_string), hashlib.sha1).hexdigest()
        return p_hash
 
    def __private_request(self, post_data):
        #fill in common post_data parameters
        time_long = int(time.time()*1000000)
        post_data['tonce'] = time_long
        post_data['accesskey'] = self.__access_key
        post_data['requestmethod'] = 'post'
 
        # If ID is not passed as a key of post_data, just use tonce
        if not 'id' in post_data:
            post_data['id'] = time_long
 
        pd_hash = self._get_params_hash(post_data)
        # must use b64 encode        
        auth_string = 'Basic '+self.__bytes_str(base64.b64encode(self.__str_bytes(self.__access_key+':'+pd_hash)))
        headers = {'Authorization': auth_string, 'Json-Rpc-Tonce': str(time_long)}
 
        #post_data dictionary passed as JSON        
        response, content = self.__http_client.request(self.__url, "POST", json.dumps(post_data), headers)
 
        # check response code, ID, and existence of 'result' or 'error'
        # before passing a dict of results
        if response.status == 200:
            # this might fail if non-json data is returned
            resp_dict = json.loads(str(content, encoding="utf8"))
 
            # The id's may need to be used by the calling application,
            # but for now, check and discard from the return dict
            if str(resp_dict['id']) == str(post_data['id']):
                if 'result' in resp_dict:
                    return resp_dict['result']
                elif 'error' in resp_dict:
                    return resp_dict['error']
        else:
            # not great error handling....
            print("status:", response.status)
            print("reason:", response.reason)
 
        return None

    def get_account_info(self):
        # Get the account information of this access key
        post_data = {}
        post_data['method'] = 'getAccountInfo'
        post_data['params'] = []
        return self.__private_request(post_data)
 
    def get_market_depth(self, limit=10):
        post_data = {}
        post_data['method'] = 'getMarketDepth2'
        post_data['params'] = [limit]
        result = self.__private_request(post_data)
        try:
            return result['market_depth']
        except:
            return result
 
    def buy_order(self, price, amount):
        post_data = {}
        post_data['method'] = 'buyOrder'
        post_data['params'] = [str(price), str(amount)]
        return self.__private_request(post_data)
 
    def sell_order(self, price, amount):
        post_data = {}
        post_data['method'] = 'sellOrder'
        post_data['params'] = [str(price), str(amount)]
        return self.__private_request(post_data)
 
    def cancel_order(self, order_id):
        post_data = {}
        post_data['method'] = 'cancelOrder'
        post_data['params'] = [order_id]
        return self.__private_request(post_data)
 
    def request_withdrawal(self, currency, amount):
        post_data = {}
        post_data['method'] = 'requestWithdrawal'
        post_data['params'] = [currency, amount]
        return self.__private_request(post_data)
 
    def get_deposits(self, currency='BTC', pending=True):
        post_data = {}
        post_data['method'] = 'getDeposits'
        post_data['params'] = [currency, pending]
        return self.__private_request(post_data)
 
    def get_orders(self, open_only=True, order_id=None):
        # this combines getOrder and getOrders
        post_data = {}
        if order_id is None:
            post_data['method'] = 'getOrders'
            post_data['params'] = [open_only]
        else:
            post_data['method'] = 'getOrder'
            post_data['params'] = [order_id]
        return self.__private_request(post_data)
 
    def get_withdrawals(self, withdrawal_id='BTC', pending=True):
        # this combines getWithdrawal and getWithdrawls
        post_data = {}
        try:
            withdrawal_id = int(withdrawal_id)
            post_data['method'] = 'getWithdrawal'
            post_data['params'] = [withdrawal_id]
        except:
            post_data['method'] = 'getWithdrawals'
            post_data['params'] = [withdrawal_id, pending]
        return self.__private_request(post_data)
 
    def get_transactions(self, trans_type='all', limit=10):
        post_data = {}
        post_data['method'] = 'getTransactions'
        post_data['params'] = [trans_type, limit]
        return self.__private_request(post_data)   
