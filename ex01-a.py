import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df=pd.read_csv('./Data/scores.csv')
#df.index=df['name']
#deldf['name']

#1반학생을출력pandas데이터프레임의추출한행의조건식을부여
#df으로부터class칼럼의속성이1인지판별하여booleanArray를추출한다.

arr_1=df['class']==1
class_1=df[arr_1]

subject=['kor','eng','mat','bio']
names=class_1['name']

#1반의과목별평균출력

#print('국어',np.average(class_1['kor']))
#print('영어',np.average(class_1['eng']))
#print('수학',np.average(class_1['mat']))
#print('과학',np.average(class_1['bio']))

#1반의성적을막대그래프출력

kor=class_1['kor']
eng=class_1['eng']
mat=class_1['mat']
bio=class_1['bio']

plt.subplot(4,1,1)
plt.ylabel('kor')
plt.xticks(range(len(class_1)),names)
plt.bar(range(len(class_1)),kor,0.5)

plt.subplot(4,1,2)
plt.ylabel('eng')
plt.xticks(range(len(class_1)),names)
plt.bar(range(len(class_1)),eng,0.5)

plt.subplot(4,1,3)
plt.ylabel('mat')
plt.xticks(range(len(class_1)),names)
plt.bar(range(len(class_1)),mat,0.5)

plt.subplot(4,1,4)
plt.ylabel('bio')
plt.xticks(range(len(class_1)),names)
plt.bar(range(len(class_1)),bio,0.5)

plt.show()