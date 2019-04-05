# 합치려고 하는 파일의 데이터 수가 일치하지 않는다. (dan을 삭제)

import numpy as np
import pandas as pd

# 서로 일치하지 않는 데이터 dan 정보도 출력하고 점수는 0으로 출력
df1 = pd.read_csv('./Data/stu01',sep="::",engine="python")
df2 = pd.read_csv('./Data/stu02',sep="::",engine="python")
df = pd.merge(df1,df2,how='outer')
print(df.fillna(0))


