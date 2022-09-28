# -*- coding: utf-8 -*-

import json

import helpers.KeyManager as KeyManager
from pai.pai_client import PaiClient


def ret_handle(ret: dict):
    print(json.dumps(ret, ensure_ascii=False))
    """
    OCR接口有白名单:
        {"code": "90004", "ok": false, "message": "调用接口的IP【120.228.6.137】不在白名单中，请在接口IP白名单中进行设置"}
        
    
    """


if __name__ == '__main__':

    app_id, app_key = KeyManager.get_secret_key('96ad835366e04999b5e1d73a19884b4b')

    pai_client = PaiClient(app_id, app_key)

    import base64
    with open("85260295.jpg", "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read())

    response = pai_client.ocr(img_base64.decode('utf-8'))

    if 200 == response.status_code:
        try:
            ret_handle(response.json())
        except Exception as e:
            print("Ret: {}".format(response.text))
            print("Exception: ", e)
    else:
        print(response.text)
