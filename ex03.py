import pandas as pd
import numpy as np
# 연습) student01과 student02 파일의 내용으 읽어들여 각각 df1과 df2 담아봅니다.
df1 = pd.read_csv('./Data/student01',sep="::",engine="python")
df2 = pd.read_csv('./Data/student02',sep="::",engine="python")
print(df1)
print(df2)

df = pd.merge(df1,df2)
print(df)
