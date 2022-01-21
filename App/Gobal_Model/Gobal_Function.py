# -*- coding: utf-8 -*-

import time
import hmac
import base64
from settings.env import Config

class GobalFun:
    # 生成token,默认60分钟,需要与配置文件cache参数一致
    def generate_token(key, expire= Config.CACHE_DEFAULT_TIMEOUT * 60):
        ts_str = str(time.time() + expire)
        ts_byte = ts_str.encode("utf-8")
        sha1_tshexstr = hmac.new(
            key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
        token = ts_str+':'+sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
        return b64_token.decode("utf-8")

    # 验证token
    def certify_token(key, token):
        token_str = base64.urlsafe_b64decode(token).decode('utf-8')
        token_list = token_str.split(':')
        if len(token_list) != 2:
            return False
        ts_str = token_list[0]
        if float(ts_str) < time.time():
            # token expired
            return False
        known_sha1_tsstr = token_list[1]
        sha1 = hmac.new(key.encode(
            "utf-8"), ts_str.encode('utf-8'), 'sha1')
        calc_sha1_tsstr = sha1.hexdigest()
        if calc_sha1_tsstr != known_sha1_tsstr:
            # token certification failed
            return False
        # token certification success
        return True
