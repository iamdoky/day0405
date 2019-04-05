import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df = pd.read_csv('./Data/scores.csv')
# df.index = df['name']
# del df['name']

# 1반 학생을 출력 pandas 데이터 프레임의 추출한 행의 조건식을 부여
# df 으로 부터 class 칼럼의 속성이 1인지 판별하여 boolean Array를 추출한다.

# 1반의 과목별 평균 출력
print(df[df['class'] == 1])
# class_1.index = class_1['name']
# del class_1['class']
# del class_1['name']
# # print(class_1.mean())                   # 데이터분석에서는 column(열), 특성을 중요 시 한다.
# # print(class_1.mean(axis=1))             # 학생별 평균    axis = 1 행으로 평균을 내준다.(default=0)
#                                           # axis = 0은 col(열)에 대한 값 / axis = 1은 row(행)에 대한 값
# print(class_1)
# # 1반의 성적을 막대그래프 출력
# # 국어성적 조회
# # plt.bar(range(len(class_1.index)),class_1['kor'])
# # plt.xticks(range(len(class_1.index)),class_1.index)
# # plt.show()
# # class_1.plot()
# class_1.plot(kind='bar')
# plt.show()

# help(pd.DataFrame.plot)                 # Pandas 라이브러리의 DataFrame이 제공하는 plot함수에 대한 도움말...
