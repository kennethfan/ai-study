#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import torch
from torch.utils.data import DataLoader

from dlt_dataset import DltDataSet
from dlt_model import DltModel

filename = 'result.xlsx'
filepath = os.path.join(os.path.dirname(__file__), filename)

print(filepath)
column_labels = ['no', 'year', 'month', 'day', 'seq', 'week', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7']
input_columns = ['no', 'year', 'month', 'day', 'seq', 'week']
output_columns = ['n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7']
# output_columns = ['n1', 'n2', 'n3', 'n4', 'n5']
# output_columns = ['n6', 'n7']

dataset = DltDataSet(filepath, column_labels, input_columns, output_columns)
dataloader = DataLoader(dataset, 1)
input_len = len(input_columns)
output_len = len(output_columns)
hidden_len = int((input_len + output_len) / 2)
model = DltModel(len(input_columns), 7, len(output_columns))

criterion = torch.nn.MSELoss(reduction='sum')
optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

max_epoch = 30
for epoch in range(max_epoch):
    cnt = 0
    sum_loss = 0.0
    for i, batch in enumerate(dataloader):
        x, y = batch[0][0], batch[1][0]
        x = x.to(torch.float32)
        y = y.to(torch.float32)
        y_pred = model(x)

        loss = criterion(y_pred, y)
        # if i % 100 == 99:
        #     print(i, loss.item())
        sum_loss += loss.item()
        cnt += 1

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f'epoch={epoch}, avg_loss={sum_loss / cnt}')
