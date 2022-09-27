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


if __name__ == '__main__':
    print("JSON with Python!")

    convert_json_string()

    read_json_file("employee.json")
