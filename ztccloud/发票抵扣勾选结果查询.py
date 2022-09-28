# -*- coding: utf-8 -*-

import json

from pai.pai_client import PaiClient
import helpers.KeyManager as KeyManager


def ret_handle(ret: dict):
    # print(json.dumps(ret, ensure_ascii=False))
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
        if 'invoicesData' in data:
            invoices = data.pop('invoicesData')
            print(json.dumps(data, ensure_ascii=False), '\n\n发票列表: ')
            for i, invoice in enumerate(invoices):
                print('{}. {}'.format(i + 1, json.dumps(invoice, ensure_ascii=False)))

    if 'totalRows' in ret:
        print("\nTotal Rows: {}".format(ret.pop('totalRows')))


if __name__ == '__main__':

    app_id = '8545f14352eb41df9d112cefc3958086'
    app_key = KeyManager.get_secret_key(app_id)

    pai_client = PaiClient(app_id, app_key)

    response = pai_client.get_select_auth_result('91440300708437873H20220701209226')

    if 200 == response.status_code:
        try:
            ret_handle(response.json())
        except Exception as e:
            print("Ret: {}".format(response.text))
            print("Exception: ", e)
    else:
        print(response.text)
