#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from torch.utils.data import Dataset


class DltDataSet(Dataset):
    def __init__(self, filename, names, x_columns, y_columns):
        df = pd.read_excel(filename, names=names)
        self.size = df.shape[0]
        self.x_ds = df[x_columns].values
        self.y_ds = df[y_columns].values

    def __len__(self):
        return self.size

    def __getitem__(self, idx):
        x = self.x_ds[idx]
        y = self.y_ds[idx]

        return x, y
