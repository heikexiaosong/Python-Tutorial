# -*- coding: utf-8 -*-

import json

import helpers.KeyManager as KeyManager
from pai.pai_client import PaiClient


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
        msg = data.pop('msg')
        print(msg)

        print(json.dumps(data.pop('fpxx'), ensure_ascii=False))
        '''
        {
            "xfsbh": "44030611DK00193",
            "fpmxlb": [
                {
                    "ssflbm": "1060401000000000000",
                    "ggxh": "",
                    "se": "11.65",
                    "dw": "个",
                    "hwmc": "*文具*工作卡",
                    "dj": "7.76700000",
                    "sl": "50.00000000",
                    "je": "388.35",
                    "slv": "3"
                }
            ],
            "gfmc": "深圳市中兴新云服务有限公司",
            "gfdz": "深圳市前海深港合作区前湾一路1号A栋201室（入驻深圳市前海商务秘书有限公司）",
            "gfyhzh": "中信银行深圳市民中心支行 8110301013100278455",
            "gfkhhdz": "中信银行深圳市民中心支行",
            "yxse": "11.65",
            "xfdh": "27679910",
            "fpbz": "自愿放弃免征政策 代开企业税号:91440300350069577K 代开企业名称:深圳市伟创礼品有限公司",
            "gfdh": "0755-86541249",
            "kprq": "20220922",
            "sfdbts": "0",
            "xfdzdh": "深圳市宝安区西乡街道宝田工业区宝树工业园1栋5楼 27679910",
            "xfkhhdz": "",
            "gfkhhzh": "8110301013100278455",
            "rzfs": "",
            "gfsbh": "91440300MA5EXWHW6F",
            "rzlx": "0",
            "fpdm": "4403222130",
            "xfkhhzh": "344036220900674590",
            "fplx": "01",
            "fpse": "11.65",
            "xfyhzh": "344036220900674590",
            "rzrq": "",
            "fpzt": "0",
            "fpje": "388.35",
            "gfdzdh": "深圳市前海深港合作区前湾一路1号A栋201室（入驻深圳市前海商务秘书有限公司） 0755-86541249",
            "rzzt": "0",
            "xfmc": "国家税务总局深圳市宝安区税务局西乡税务所代开八",
            "xfdz": "深圳市宝安区西乡街道宝田工业区宝树工业园1栋5楼",
            "fphm": "04520486",
            "fpjshj": "400.00",
            "jym": "",
            "skssq": ""
        }
        '''


if __name__ == '__main__':

    app_id = '96ad835366e04999b5e1d73a19884b4b'
    app_key = KeyManager.get_secret_key(app_id)

    pai_client = PaiClient(app_id, app_key)

    response = pai_client.gather_single('04520486', '4403222130', '91440300MA5EXWHW6F', '01')

    if 200 == response.status_code:
        try:
            ret_handle(response.json())
        except Exception as e:
            print("Ret: {}".format(response.text))
            print("Exception: ", e)
    else:
        print(response.text)
