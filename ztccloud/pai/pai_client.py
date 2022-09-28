# -*- coding: utf-8 -*-
import json

import requests

import helpers.pai as pai


def pai_endpoint(path, method='POST'):
    def decorator(function):
        def wrapper(*args, **kwargs):
            kwargs.update({
                'path': path,
                'method': method
            })
            return function(*args, **kwargs)

        wrapper.__doc__ = function.__doc__
        return wrapper

    return decorator


class PaiClient():
    """
    派平台接口客户端

    """

    def __init__(self, app_id, app_key):
        self.app_id = app_id
        self.app_key = app_key

    def build_query_params(self, data, *args):
        """

        :param data:
        :param args:
        :return:
        """
        return pai.build_param(data, self.app_id, self.app_key)

    def _check_version(self, path):
        return path

    def _request(self, path: str, data: dict = None, params: dict = None) -> object:
        if params is None:
            params = {}
        if data is None:
            data = {}

        # data = {'appId': '8285b1e58f864352a64725f7506b6f6e', 'data': '{"batchNo": "91430000780850865920220901195412", "nsrsbh": "914300007808508659"}', 'format': 'json', 'noncestr': 'fd1da5a4-3e8c-11ed-9276-d8bbc1281180', 'timestamp': '2022-09-28 01:51:18', 'version': 'V1.0', 'sign': 'YEphn6Y+MO6pRz+Ssw049Z3/ph4='}

        print(json.dumps(data))

        #

        self.method = params.pop('method', data.pop('method', 'POST'))
        self.endpoint = 'http://einvoice.ztccloud.com.cn'
        # res = request(self.method,
        #               self.endpoint + self._check_version(path),
        #               params=params,
        #               json=data if data and self.method in ('POST', 'PUT', 'PATCH') else None)
        return requests.post(self.endpoint + self._check_version(path), json=data)

    @pai_endpoint('/api/csInputDeduct/selectBuyInvs')
    def get_dzk_item(self, batch_no: str, **kwargs) -> object:
        """
        获取底帐库发票信息

        get_dzk_item(self, batch_no: str, **kwargs) -> object
        Returns a specified item and its attributes.

        Examples:
            literal blocks::

                res = PaiClient().get_item('91430000780850865920220901195412')

        Args:
            batch_no: str
            **kwargs:

        Returns:
            GetCatalogItemResponse:
        """

        record = {
            'batchNo': batch_no,
            'nsrsbh': batch_no[:18]
        }

        return self._request(kwargs.pop('path'), data=self.build_query_params(record, kwargs))

    @pai_endpoint('/api/incomingCertification/queryStateSync')
    def get_changed_state_items(self, start_time: str, end_time: str, **kwargs) -> object:
        """
        获取底帐库发票变更列表

        get_changed_state_items(self, batch_no: str, **kwargs) -> object
        Returns a specified item and its attributes.

        Examples:
            literal blocks::

                res = PaiClient().get_changed_state_items('2022-07-01', '2022-07-02')

        Args:
            start_time: str
            end_time: str
            **kwargs:

        Returns:
            GetCatalogItemResponse:
        """

        record = {
            "startTime": start_time,
            "endTime": end_time
        }
        return self._request(kwargs.pop('path'), data=self.build_query_params(record, kwargs))

    @pai_endpoint('/api/csInputDeduct/enterpriseArchives')
    def get_activated_tax_period(self, buyer_number: str, **kwargs) -> object:
        """
        查询税款所属期

        get_activated_tax_period(self, buyer_number: str, **kwargs) -> object
        Returns a specified item and its attributes.

        Examples:
            literal blocks::

                res = PaiClient().get_activated_tax_period('91150602MA13NM9N2X')

        Args:
            buyer_number: str
            **kwargs:

        Returns:
            GetCatalogItemResponse:
        """

        record = {
            "nsrsbh": buyer_number
        }
        return self._request(kwargs.pop('path'), data=self.build_query_params(record, kwargs))

    @pai_endpoint('/api/csInputDeduct/selectAuthResult')
    def get_select_auth_result(self, batch_no: str, **kwargs) -> object:
        """
        发票抵扣勾选结果查询

        get_select_auth_result(self, buyer_number: str, **kwargs) -> object
        Returns a specified item and its attributes.

        Examples:
            literal blocks::

                res = PaiClient().get_select_auth_result('91440300708437873H20220701209226')

        Args:
            batch_no: str
            **kwargs:

        Returns:
            GetCatalogItemResponse:
        """

        record = {
            'batchNo': batch_no,
            'nsrsbh': batch_no[:18]
        }
        return self._request(kwargs.pop('path'), data=self.build_query_params(record, kwargs))

    @pai_endpoint('/api/incomingCertification/gatherSingle')
    def gather_single(self, fphm: str, fpdm: str, buyer_number: str, fplx: str, **kwargs) -> object:
        """
        单票查询

        gather_single(self, buyer_number: str, **kwargs) -> object
        Returns a specified item and its attributes.

        Examples:
            literal blocks::

                res = PaiClient().gather_single('91440300708437873H20220701209226')

        Args:
            fphm: str
            fpdm: str
            buyer_number: str
            fplx: str
            **kwargs:

        Returns:
            GetCatalogItemResponse:
        """

        record = {
            'fpdm': fpdm,
            'fphm': fphm,
            'nsrsbh': buyer_number,
            'fplx': fplx
        }
        return self._request(kwargs.pop('path'), data=self.build_query_params(record, kwargs))
