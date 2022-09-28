# -*- coding: utf-8 -*-

import json

from pai.pai_client import PaiClient
import helpers.KeyManager as KeyManager


def ret_handle(ret: dict):
    """
    Example: {
                "data": {"ssq": "202209", "gxfw": "20170101-20220930", "dqjzsj": "20221025"},
                "returnStateInfo": {"returnMessage": "调用成功", "returnCode": "0000"},
                "ok": true
            }
    :param ret:
    :return:
    """
    ok = ret.pop('ok')
    if not ok:
        msg = '' if 'message' not in ret else ret.pop('message')
        raise AssertionError(msg)

    return_state_info = ret.pop('returnStateInfo')
    return_code = return_state_info["returnCode"]
    if return_code != '0000':
        msg = '' if 'returnMessage' not in return_state_info else return_state_info.pop('returnMessage')
        raise AssertionError(msg)

    data = None if 'data' not in ret else ret.pop('data')
    if data is not None:
        print(json.dumps(data, ensure_ascii=False))


if __name__ == '__main__':

    app_id, app_key = KeyManager.get_secret_key('8285b1e58f864352a64725f7506b6f6e')

    pai_client = PaiClient(app_id, app_key)

    response = pai_client.get_activated_tax_period('91150602MA13NM9N2X')

    if 200 == response.status_code:
        try:
            ret_handle(response.json())
        except Exception as e:
            print("Ret: {}".format(response.text))
            print("Exception: ", e)
    else:
        print(response.text)
