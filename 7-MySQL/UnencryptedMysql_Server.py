# -*- coding: UTF-8 -*-
from socket import *
import pandas as pd
import pickle

filename = '../data/data.csv'


def find(message):
    df = pd.read_csv(filename)
    ans_message = []
    for index, row in df.iterrows():
        if row['date'] == message:
            ans_message.append(row['reviewer_name'])
    return ans_message


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
