# -*- coding: utf-8 -*-

import base64
import hmac
import json
import time
import uuid
from hashlib import sha1


def hash_hmac(key, code, sha1=sha1):
    """
    使用 HMAC-SHA1 签名方法对对encryptText进行签名

    :param key:
    :param code:
    :param sha1:
    :return:
    """
    hmac_code = hmac.new(key.encode(), code.encode(), sha1)
    msg = base64.b64encode(hmac_code.digest())
    return msg.decode('UTF-8')


def encrypt(payload, key):
    build = []
    for k, v in payload.items():
        build.append("{}={}".format(k, v))
    return hash_hmac(key, "&".join(build))


def build_param(record, app_id, app_key):
    payload = {
        "appId": app_id,
        "data": json.dumps(record),
        "format": "json",
        "noncestr": str(uuid.uuid1()),
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "version": "V1.0"
    }
    encrypt_text = encrypt(payload, app_key)
    payload["sign"] = encrypt_text
    return payload
