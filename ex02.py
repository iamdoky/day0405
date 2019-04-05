import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터의 수가 많으면 전체를 파악하기 어려워 앞 또는 뒤에서 몇개만 추출하여 데이터를 파악
# print(df.head(1))    # head()는 앞에서 default 5개   (1)은 옵션
# print(df.tail(1))    # tail()는 앞에서 default 5개   (1)은 옵션


# 수학점수가 평균이하인 모든학생의 성적을 막대그래프로 출력
df = pd.read_csv('./data/scores.csv')
df.index = df['name']
del df['name']
del df['class']
lower_mean = df[df['mat'] <= df['mat'].mean()].plot(kind='bar',colormap='PRGn')
plt.show()










