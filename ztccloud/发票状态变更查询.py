# -*- coding: utf-8 -*-

import json

from pai.pai_client import PaiClient
import helpers.KeyManager as KeyManager


def ret_handle(ret: dict):
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
        if 'msg' in data:
            raise AssertionError(data['msg'])

        if 'invoicesData' in data:
            invoices = data.pop('invoicesData')
            for i, invoice in enumerate(invoices):
                print('{}. {}'.format(i + 1, json.dumps(invoice, ensure_ascii=False)))


if __name__ == '__main__':

    app_id = '2930f2f11f484eabbcb0cff2600874db'
    app_key = KeyManager.get_secret_key(app_id)

    pai_client = PaiClient(app_id, app_key)

    response = pai_client.get_changed_state_items('2022-09-27', '2022-09-28')

    if 200 == response.status_code:
        try:
            ret_handle(response.json())
        except Exception as e:
            print("Ret: {}".format(response.text))
            print("Exception: ", e)
    else:
        print(response.text)
