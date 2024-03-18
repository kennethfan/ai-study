#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pandas as pd

# 创建一个示例 DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50],
        'C': [100, 200, 300, 400, 500]}
df = pd.DataFrame(data)

# 获取 DataFrame 的行数
num_rows = df.shape[0]

print("DataFrame 的行数:", num_rows)