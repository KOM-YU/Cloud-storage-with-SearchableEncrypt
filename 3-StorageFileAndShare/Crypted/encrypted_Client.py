# -*- coding: UTF-8 -*-
import socket
import pickle
import fileinput
import pandas as pd
import time

from pypbc import *
import hashlib

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


# 密钥生成算法，输入安全参数qbits和rbits，返回[params, g, pk, sk]
def KeyGen(qbits, rbits):
    params = Parameters(qbits=qbits, rbits=rbits)
    pairing = Pairing(params)
    g = Element.random(pairing, G2)
    sk = Element.random(pairing, Zr)
    pk = Element(pairing, G2, value=g ** sk)
    return [params, g, pk, sk]


# PEKS算法，输入公共参数[params, g]，公钥pk，关键字word，返回[A, B] （具体参考论文）
def PEKS(params, g, pk, word):
    pairing = Pairing(params)
    hash_value = Element.from_hash(pairing, G1, word)
    r = Element.random(pairing, Zr)
    temp = pairing.apply(hash_value, pk ** r)
    return [g ** r, hashlib.sha256(str(temp).encode("utf8")).hexdigest()]


# 陷门生成算法，输入公共参数[params]，私钥sk，待查关键字word，返回陷门td
def Trapdoor(params, sk, word):
    pairing = Pairing(params)
    hash_value = Element.from_hash(pairing, G1, word)
    return hash_value ** sk


# 测试算法，输入公共参数[params]，公钥pk，S=[A, B]，陷门td，返回布尔值True/False
def Test(params, pk, S, td):
    pairing = Pairing(params)
    [A, B] = S
    hash_value = Element.from_hash(pairing, G1, "test")
    td = Element(pairing, G1, value=str(td))
    temp = pairing.apply(td, A)
    return hashlib.sha256(str(temp).encode("utf8")).hexdigest() == B
[params, g, pk, sk] = KeyGen(1024, 180)
pairing = Pairing(params)


start = time.time()

HOST = '39.96.34.16'
PORT = 6788

filename = 'query.csv'
filename2='ghost-private.pem'

keyword_list = []
df = pd.read_csv(filename)
for index, row in df.iterrows():
    keyword_list.append(row['name'])

for i in range(6):
    keywords = keyword_list[i % len(keyword_list)]
    #keywords = input('输入搜索关键词：')
    if(keywords == 'close'):
        break
    file=bytes.decode(base64.b64encode(keywords.encode('utf-8')))
    print(file)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s :
        s.connect((HOST, PORT))
        s.sendall(file.encode())

        recv_data = []
        while True:
            packet = s.recv(4096)
            if not packet:
                break
            recv_data.append(packet)
        ans = pickle.loads(b"".join(recv_data))
        print(ans)
        fh = open(keywords, 'w',encoding='utf-8')
        fh.write(ans)
        fh.close()
        
    s.close()

end = time.time()
print('Time cost = %fs' % (end - start))




