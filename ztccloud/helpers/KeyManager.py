# -*- coding: utf-8 -*-

import json

JSON_FILE_NAME = 'app_key.json'


def get_secret_key(key):
    """
    获取key对应的密钥
    :param key:
    :return:
    """
    if len(key) == 0:
        return ''

    f = open(JSON_FILE_NAME, )
    key_dict = json.load(f)
    f.close()

    return key_dict[key] if key in key_dict else ''


def sync_app_key():
    """
    从派平台同步appkey信息

    :return:
    """

    import pymysql

    conn = pymysql.connect(
        host='ztefsscinvoiceo.mysql.rds.aliyuncs.com',
        user='zfs_readonly',
        password="Ztefssc_2021",
        db='invoice_check',
    )

    cur = conn.cursor()

    # Select query
    cur.execute("select APP_ID, ENCRYPT_KEY from company")
    records = cur.fetchall()
    conn.close()

    key_dict = {}
    for record in records:
        print(record)
        key_dict[record[0]] = record[1]

    print("records: ", len(records))
    print("map: ", len(key_dict.keys()))

    with open(JSON_FILE_NAME, "w") as outfile:
        # ensure_ascii=False: 不使用ascii编码
        json.dump(key_dict, outfile, ensure_ascii=False, indent=4)


# Driver Code
if __name__ == "__main__":
    secret_key = get_secret_key('f542407f7c554f43adaafcb35f377e4f')
    print('secret_key: ', secret_key)
