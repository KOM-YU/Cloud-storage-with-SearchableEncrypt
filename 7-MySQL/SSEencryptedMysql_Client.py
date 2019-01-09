# -*- coding: UTF-8 -*-
import socket
import pickle
import fileinput
import pandas as pd
import time
import json
from base64 import b64decode
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

start = time.time()

#HOST = '127.0.0.1'
HOST = '39.96.34.16'
PORT = 6788

filename = '../data/query.csv'


keyword_list = []
df = pd.read_csv(filename)
for index, row in df.iterrows():
    keyword_list.append(row['date'])

key = pad(b'secret', 16)

for i in range(100):
    keywords = keyword_list[i % len(keyword_list)]
    #keywords = input('输入搜索关键词：')
    if(keywords == 'close'):
        break
    data = (keywords).encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        s.connect((HOST, PORT))
        s.sendall(ct_bytes)
        recv_data = []
        while True:
            packet = s.recv(4096)
            if not packet:
                break
            recv_data.append(packet)
        ans = pickle.loads(b"".join(recv_data))
        with open("SSEencrypted_Result.txt", "w", encoding='utf-8') as output_file:
            for line in ans:
                output_file.write(b64decode(str(line)[2:-1]).decode('utf-8'))
                output_file.write("\n")
    s.close()

end = time.time()
print('Time cost = %fs' % (end - start))



