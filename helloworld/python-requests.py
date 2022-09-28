# -*- coding: UTF-8 -*-
import requests


def write_to_csv(datas, out_file_name):
    """
    json数据写入csv文件
    """

    import pathlib
    import os

    dir_name = os.path.dirname(out_file_name)
    path = pathlib.Path(dir_name)
    print(path, dir_name)
    if not path.exists():
        os.makedirs(path)

    import csv
    data_file = open(out_file_name, 'w')

    csv_writer = csv.writer(data_file)
    # 写入csv标题行
    header = datas[0].keys()
    csv_writer.writerow(header)

    for data in datas:
        # 写入csv数据行
        csv_writer.writerow(data.values())

    data_file.close()


if __name__ == '__main__':
    print("Python’s Requests Library.")

    params = {
        "appId": "e558aa0376d24d12bd81b426a44e8560",
        "encryptKey": "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKFzjF0wnZEpN0GShDy5ZBuO/tRSa4yvbFmAolfRrmlpaVYXnC3Zi2vgDKLvQ3+dArZUwrz6chPqbukefupGo2MCAwEAAQ==",
        "nsrsbh": "12320585MB1782024B",
        "batchNo": "",
        "fphm": ""
    }
    response = requests.get('http://114.55.6.229:9080/api/pai/ledgers', params=params)
    if response.status_code != 200:
        print('[{}]{}'.format(response.status_code, response.reason))
        exit(0)


    print(response.status_code)
    print(response.headers)
    print(response.headers["Content-Type"])

    json_response = response.json()
    print(json_response)
    write_to_csv(json_response['data'], 'data/底帐库记录-12320585MB1782024B.csv')
