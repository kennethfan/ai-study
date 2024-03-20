#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from datetime import datetime

import pandas as pd
import requests


def result_list(base_url: str, max_page: int):
    for i in range(max_page, 0, -1):
        url = f'{base_url}{i}'
        response = requests.get(url)

        # 检查响应状态码
        if response.status_code == 200:
            # 处理响应数据
            data = response.json()
            yield data['value']['list'][::-1]
        else:
            raise IOError(f"get response from {url} error")


def parse_page_result(page_data: list):
    data_list = []
    for row in page_data:
        data = []
        data.append(int(row['lotteryDrawNum']))

        date = datetime.strptime(row['lotteryDrawTime'], "%Y-%m-%d")
        data.append(date.year)
        data.append(date.month)
        data.append(date.day)
        data.append(date.weekday())

        num_str_list = row['lotteryDrawResult'].split(' ')
        num_list = list(map(lambda x: int(x), num_str_list))
        data.extend(num_list)

        data_list.append(data)
    return data_list


def load_data(excel_path: str, base_url: str, max_page: int):
    filepath = os.path.join(os.path.dirname(__file__), excel_path)
    if os.path.exists(filepath):
        os.remove(filepath)

    size = 0
    with pd.ExcelWriter(excel_path, mode='w') as writer:
        for page_result in result_list(base_url, max_page):
            record_list = parse_page_result(page_result)
            pd.DataFrame(record_list).to_excel(writer, index=False, startrow=size, header=None)
            size += len(record_list)


if '__main__' == __name__:
    data_base_url = 'https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=85&provinceId=0&pageSize=30&isVerify=1&pageNo='
    data_max_page = 85
    data_excel = 'data.xlsx'

    load_data(data_excel, data_base_url, data_max_page)
