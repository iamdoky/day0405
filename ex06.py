import numpy as np
import pandas as pd

# movies.dat
# 영화id::영화제목::장르
# 1::Toy Story (1995)::Animation|Children's|Comedy

# users.dat
# 사용자id::성별::나이::직업::우편번호
# 1::F::1::10::48067

# ratings.dat
# 사용자id::영화id::별점::tlrks
# 1::1193::5::978300760

movies = pd.read_csv('../ml-1m/movies.dat',sep="::",engine='python',header=None,names=['movie_id','title','genre'])
users = pd.read_csv('../ml-1m/users.dat',sep="::",engine='python',header=None,names=['user_id','gender','age','job','addr'])
ratings = pd.read_csv('../ml-1m/ratings.dat',sep="::",engine='python',header=None,names=['user_id','movie_id','rating','timestamp'])
# print(movie.head(1))
# print(user.head(1))
# print(ratings.head(1))
# m_u_r = pd.merge(movie,user,ratings, how='outer')
df = pd.merge(pd.merge(movies,ratings),users,how='outer')
print(df.head(1))



