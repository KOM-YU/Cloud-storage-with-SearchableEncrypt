import numpy as np
import pandas as pd

#处理数据
'''
df = pd.read_csv('reviews.csv')

df.drop(['listing_id','id'], axis=1, inplace=True)

df.to_csv(r'data.csv',index=False)
'''

#生成询问
df = pd.read_csv('data.csv')

data = df.drop_duplicates(['date'])

data.drop(['reviewer_name', 'reviewer_id', 'comments'], axis=1, inplace=True)
data['date'] = pd.to_datetime(data['date'])
#print(data.dtypes)
data.to_csv(r'query.csv', date_format='%Y-%m-%d', index=False)