from day0405 import ex07
import pandas as pd
import numpy as np
df = ex07.data()

# 남자의 평점의 평균
# m = df[df['gender']  == 'M']['rating'].mean()

# 여자의 평점의 평균
# f = df[df['gender']  == 'F']['rating'].mean()

# Toy Story (1995)
# 토이스토리 평점의 평균
# toy_m = df[df['title'] == 'Toy Story (1995)']['rating'].mean()

# 토이스토리 평가한 건수
# toy_l =len(df[df['title'] == 'Toy Story (1995)']['rating'])

# 토이스트리 평균 평균나이
# toy_a = df[df['title'] == 'Toy Story (1995)']['age'].mean()

# 평점 5점 이상인 영화 제목
# f = df[df['rating'] == 5]['title']

# 영화별 평균 평점을 구하여 평균값이 5점 이상인 데이터가 필요하다.
# oracle ==> group by / python = pivot table
# select title. avg(rating) from df group by title

# help(pd.pivot_table)

# ivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')
#     Create a spreadsheet-style pivot table as a DataFrame. The levels in

# 영화별 평균을 구한다 pivot_table
# p = pd.pivot_table(df,values='rating',index='title',aggfunc='mean')
# r = p[p['rating'] == 5]

# 100명 이상이 평가한 영화중에 평균평점이 5점인 영화가 있는지.
# print(len(df[df['title']=='Bittersweet Motel (2000)']))

# 영화별 평가수를 출력
p = pd.pivot_table(df,values='rating',index='title',aggfunc='count')

# 영화별 평가수가 높은 100개의 영화중에 평균 평점이 가장 높은 5개의 영화제목을 출력
# print(p.sort_values(by="rating")[::-1])
s = p.sort_values(by="rating",ascending=False)
p1 = pd.pivot_table(df,values='rating',index='title',aggfunc='mean')
rating_top100 = s.iloc[:100].index
rating_top_score= p1.sort_values(['rating'],ascending=False)

c = pd.DataFrame(rating_top100,range(100))
d = pd.merge(df,c)
e = pd.pivot_table(d,values='rating', index='title',aggfunc='mean').sort_values(by="rating",ascending=False).head()
print(e)


# 남자가 더 좋아하는 영화 5개
# 여자가 더 좋아하는 영화 5개
# 나이대별 평점의 평균
# 나이대별 성별별 평점의 평균
# 나이대별 평점이 가장 높은 영화를 뽑아봅자
