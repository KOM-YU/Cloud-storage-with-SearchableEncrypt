# -*- coding: UTF-8 -*-
from socket import *
import pandas as pd
import pickle

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

def find(message):
    data=open(message,"r",encoding='utf-8').read()
    s=''
    with open('ghost-private.pem') as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(data), key)
        s=text.decode()
        [params, g, pk, sk] = KeyGen(1024, 180)
        pairing = Pairing(params)
        S = PEKS(params, g, pk, s)
        td = Trapdoor(params, sk, message)
        res = Test(params, pk, S, td)
    return s


serverSocket = socket(AF_INET, SOCK_STREAM) 
serverPort = 6788
serverSocket.bind(('', serverPort))
#serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.listen(10)
while True:       
    print('Ready to serve...')     
    connectionSocket, addr = serverSocket.accept()
    message = connectionSocket.recv(1024).decode()
    #print(message)
    return_message = find(message)
    #print(return_message)
    send_message = pickle.dumps(return_message)
    #print(send_message)
    connectionSocket.send(send_message)
    connectionSocket.close()

serverSocket.close()
