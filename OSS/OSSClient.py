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
import requests
import oss2  # oss2包 连接阿里云OSS的工具
import urllib.request

start = time.time()

#HOST = '127.0.0.1'
HOST = '39.96.34.16'
PORT = 6788

auth = oss2.Auth('LTAISPqgTcLPkj5J', 'rprWErsk91FIW8NnNpqEisDR0O8fyu')
endpoint = 'http://oss-cn-beijing.aliyuncs.com'  # 地址
bucket = oss2.Bucket(auth, endpoint, 'lylist-test')  # 项目名称

searchlist=[]
seach_file=open("search.txt","r")
for t in seach_file.readlines():
    searchlist.append(t[:-1])
seach_file.close()

key = pad(b'secret', 16)

for i in range(500):
    keywords = searchlist[i%6]
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
            packet = s.recv(4096)
            if not packet:
                break
            
            recv_data+=packet.decode('utf-8')
        #ans = pickle.loads(b"".join(recv_data))
        
        if (recv_data!=""):
            file_url = bucket.sign_url('GET',recv_data , 60)
            with urllib.request.urlopen(file_url, timeout=30) as response, open(keywords, "w") as f_save:
                f_save.write(b64decode(response.read()).decode('utf-8'))
                f_save.flush()
                f_save.close()
        else:
            print("no such file")
    s.close()

end = time.time()
print('Time cost = %fs' % (end - start))
