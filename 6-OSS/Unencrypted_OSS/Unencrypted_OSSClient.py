# -*- coding: UTF-8 -*-
import socket
import pickle
import fileinput
import pandas as pd
import time
import requests
import oss2  # oss2包 连接阿里云OSS的工具
import urllib.request

start = time.time()

#HOST = '127.0.0.1'
HOST = '39.96.34.16'
PORT = 6788

filename = 'query.csv'
filename2='ghost-private.pem'

auth = oss2.Auth('LTAISPqgTcLPkj5J', 'rprWErsk91FIW8NnNpqEisDR0O8fyu')
endpoint = 'http://oss-cn-beijing.aliyuncs.com'  # 地址
bucket = oss2.Bucket(auth, endpoint, 'lylist-test')  # 项目名称

keyword_list = []
df = pd.read_csv(filename)
for index, row in df.iterrows():
    keyword_list.append(row['name'])

for i in range(500):
    keywords = keyword_list[i % len(keyword_list)]
    #keywords = input('输入搜索关键词：')
    if(keywords == 'close'):
        break
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        s.connect((HOST, PORT))
        s.sendall(keywords.encode())

        recv_data = []
        while True:
            packet = s.recv(4096)
            if not packet:
                break
            recv_data.append(packet)
        ans = pickle.loads(b"".join(recv_data))
        file_url = bucket.sign_url('GET',str(ans).encode('utf-8') , 60)
        with urllib.request.urlopen(file_url, timeout=30) as response:
            fh = open('Uncrypted'+keywords, 'w',encoding='utf-8')
            fh.write(response.read().decode('utf-8'))
            fh.close()
        
    s.close()

end = time.time()
print('Time cost = %fs' % (end - start))
