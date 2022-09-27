# -*- coding: UTF-8 -*-

import json


def convert_json_string():
    """
    JSON string 转换成 dict
    """
    employee = '{"name": "Nitin", "department":"Finance", "company":"GFG"}'
    employee_dict = json.loads(employee)
    print("Type of data: ", type(employee_dict))

    print(employee_dict)
    for key, val in employee_dict.items():
        print(key, val, sep=': ')


def read_json_file(filename):
    """
    读取 JSON 文件

    :rtype: object
    :param filename:
    """
    f = open(filename, )
    data = json.load(f)
    f.close()

    print(data)
    for key, val in data.items():
        print(key, val, sep=': ')


def writing_json_string(out_file_name):
    """
    写入JSON文件
    """

    dictionary = {
        "code": "430100",
        "name": "长沙市",
        "province": "湖南省"
    }

    with open(out_file_name, "w") as outfile:
        # ensure_ascii=False: 不使用ascii编码
        json.dump(dictionary, outfile, ensure_ascii=False)

def format_json_string():
    """
    格式化 JSON
    """

    dictionary = {
        "code": "430100",
        "name": "长沙市",
        "province": "湖南省"
    }
    print(type(dictionary), dictionary)
    json_formatted_str = json.dumps(dictionary, ensure_ascii=False)
    print(type(json_formatted_str), json_formatted_str)


if __name__ == '__main__':
    print("JSON with Python!")

    convert_json_string()

    read_json_file("employee.json")

    writing_json_string("xzqh.json")

    format_json_string()
