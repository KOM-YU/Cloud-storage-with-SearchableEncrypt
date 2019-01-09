# -*- coding: UTF-8 -*-
import socket
import pickle
import fileinput
import pandas as pd
import time

start = time.time()

HOST = '39.96.34.16'
PORT = 6788

filename = 'query.csv'
filename2='ghost-private.pem'

keyword_list = []
df = pd.read_csv(filename)
for index, row in df.iterrows():
    keyword_list.append(row['name'])
for j in range(167):
    for i in range(6):
        keywords = keyword_list[i % len(keyword_list)]
        #keywords = input('输入搜索关键词：')
        if(keywords == 'close'):
            break
        print(keywords)
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
            #print(ans)
            fh = open('Uncrypted'+keywords, 'w',encoding='utf-8')
            fh.write(ans)
            fh.close()
            
        s.close()

end = time.time()
print('Time cost = %fs' % (end - start))




