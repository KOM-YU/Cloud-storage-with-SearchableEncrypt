# -*- coding: UTF-8 -*-
from socket import *
import pandas as pd
import pickle
from base64 import b64decode
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import json

filename = './data/EncryptedFileName.txt'

def find(ct_bytes):
    L1 = ct_bytes[:8]
    hash_object1 = SHA256.new(L1+b'secret')
    hashkey = hash_object1.digest()
    ans_message=''
    EncryptedFileName=open(filename,"r")
    for t in EncryptedFileName.readlines():
        tk=b64decode(t[:-4])
        c = bytearray(len(ct_bytes))
        for i in range(len(ct_bytes)):
            c[i] = ct_bytes[i] ^ tk[i]
        L = c[:8]
        R = c[8:]

        hash_object = SHA256.new(L+hashkey)
        hash = hash_object.digest()
        if (hash[:8] == R) :
            ans_message=t[:-1]
            print()
            return ans_message


serverSocket = socket(AF_INET, SOCK_STREAM) 
serverPort = 6788
serverSocket.bind(('', serverPort))
serverSocket.listen(10)
while True:       
    print('Ready to serve...')     
    connectionSocket, addr = serverSocket.accept()
    ct_bytes = connectionSocket.recv(1024)
    #print(message)
    return_message = find(ct_bytes)
    #print(return_message)
    #send_message = pickle.dumps(return_message)
    #print(send_message)
    connectionSocket.send(return_message.encode('utf-8'))
    connectionSocket.close()

serverSocket.close()
