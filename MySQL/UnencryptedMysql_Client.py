# -*- coding: UTF-8 -*-
import socket
import pickle
import fileinput
import pandas as pd
import time

start = time.time()

HOST = '39.96.34.16'
PORT = 6788

filename = '../data/query.csv'


keyword_list = []
df = pd.read_csv(filename)
for index, row in df.iterrows():
    keyword_list.append(row['date'])


for i in range(100):
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
        with open("Unencrypted_Result.txt", "w", encoding='utf-8') as output_file:
            output_file.write('\n'.join(str(line) for line in ans))
            output_file.write("\n")
    s.close()

end = time.time()
print('Time cost = %fs' % (end - start))




