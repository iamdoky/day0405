# 연습) 고객 영화 별점 파일을 읽어들여 하나의 DataFrame으로 반환하는 함수를 만들고 호출.

import numpy as np
import pandas as pd
def data():
    movies = pd.read_csv('../ml-1m/movies.dat',sep="::",engine='python',header=None,names=['movie_id','title','genre'])
    users = pd.read_csv('../ml-1m/users.dat',sep="::",engine='python',header=None,names=['user_id','gender','age','job','addr'])
    ratings = pd.read_csv('../ml-1m/ratings.dat',sep="::",engine='python',header=None,names=['user_id','movie_id','rating','time'])

    df = pd.merge(pd.merge(movies,ratings),users)
    return df
