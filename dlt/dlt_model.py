#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch
import torch.nn as nn


class DltModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(DltModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # 第一个全连接层后接 ReLU 激活函数
        x = self.fc2(x)  # 第二个全连接层，没有激活函数
        return x
