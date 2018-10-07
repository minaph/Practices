# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from decimal import Decimal
from scipy import stats

"""
宝くじの期待値を計算するプログラム。
別表5.2.csvにくじの各等の賞金と本数が記載されている。上から一等二等三等…、左が賞金、右が収録本数
"""

fn="宝くじ.csv"
df=pd.read_csv(fn,header=None,engine="python",encoding="utf-8")
dict_name={0:"当選金",1:"本数"}
df=df.rename(columns=dict_name)
df=df.applymap(lambda x: Decimal(x))

# 別表には記載されていないが、くじの総数は1300万本。

df["相対度数"]=df["本数"]/13000000


df["temp1"]=df["相対度数"]*df["当選金"]
result=df["temp1"].sum()


print(f"当選金の期待値：{result}\nその他のデータ一覧：")
print(df)
