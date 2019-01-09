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

seach_file=open("search.txt","r")

key = pad(b'secret', 16)

serachlist=[]
seach_file=open("search.txt","r")
for t in seach_file.readlines():
    serachlist.append(t[:-1])
seach_file.close()

for i in range(1000):
    keywords = serachlist[i%6]
    #keywords = input('输入文件名：')
    if(keywords == 'close'):
        break
    data = (keywords[:-4]).encode('utf-8')
    cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        s.connect((HOST, PORT))
        s.sendall(ct_bytes)
        recv_data = ""
        while True:
            packet = s.recv(8192)
            if not packet:
                break
            recv_data+=packet.decode('utf-8')
        #ans = pickle.loads(b"".join(recv_data))
        #print(recv_data)
        with open(keywords, "w") as output_file:
            output_file.write(b64decode(recv_data).decode('utf-8'))
    s.close()
    #print(i)

end = time.time()
print('Time cost = %fs' % (end - start))
