# -*- coding: UTF-8 -*-
from socket import *
import pandas as pd
import pickle


def find(message):
    data=open(message,"r",encoding='utf-8').read()
    return data

serverSocket = socket(AF_INET, SOCK_STREAM) 
serverPort = 6788
serverSocket.bind(('', serverPort))
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
