# -*- coding: utf-8 -*-

import json

from pai.pai_client import PaiClient
import helpers.KeyManager as KeyManager


def ret_handle(ret: dict):
    """
    Example: {
                "data": {
                    "ssq": "202209",
                    "batchNo": "91340400MA2RBH7M6W20220916077916",
                    "tjjg": "01=0=0=0=0=0=0;03=0=0=0=0=0=0;08=0=0=0=0=0=0;14=0=0=0=0=0=0;17=0=0=0=0=0=0;24=0=0=0=0=0=0;30=0=0=0=0=0=0;80=0=0=0=0=0=0;83=0=0=0=0=0=0;99=0=0=0=0=0=0;",
                    "tjzt": "1",
                    "failReason": "01",
                    "tjsj": "2022-09-16 03:24:01"
                },
                "returnStateInfo": {
                    "returnCode": "0000",
                    "returnMessage": "查询成功"
                },
                "ok": true
            }

    :param ret:
    :return:
    """

    print(json.dumps(ret, ensure_ascii=False, indent=4))

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
        fail_reason = data.get('failReason')
        if fail_reason == '01':
            print("执行成功")
            tjjg = data.get('tjjg')
            statistics_datas = None if tjjg is None else str.split(tjjg, ';')
            print('statistics_data: ', statistics_datas)
            if statistics_datas is not None:
                print(['发票类型', '抵扣发票份数', '抵扣总金额', '抵扣总有效税额', '不抵扣发票份数', '不抵扣总金额',
                       '不抵扣总有效税额'])
                for statistics_data in statistics_datas:
                    if len(statistics_data) == 0:
                        continue
                    # 发票类型=抵扣发票份数=抵扣总金额=抵扣总有效税额=不抵扣发票份数=不抵扣总金额=不抵扣总有效税额
                    # 01=0=0=0=0=0=0
                    statistic_ret = str.split(statistics_data, '=')
                    print(statistic_ret)




        else:
            print("Fail Reason: {}".format(fail_reason))





if __name__ == '__main__':

    app_id, app_key = KeyManager.get_secret_key('8892ed755bba48dcb2e2f40afecb8cf5')

    pai_client = PaiClient(app_id, app_key)

    response = pai_client.query_statistics_deduct('91340400MA2RP30P4Q20220831003250')

    if 200 == response.status_code:
        try:
            ret_handle(response.json())
        except Exception as e:
            print("Ret: {}".format(response.text))
            print("Exception: ", e)
    else:
        print(response.text)
