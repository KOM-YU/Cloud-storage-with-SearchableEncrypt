#coding=utf-8
import pandas as pd
from numpy import *
import operator
import numpy as np
import csv
import rsa
import base64
# 公钥可搜索加密-2004-Boneh


from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA


random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)
# ghost的秘钥对的生成

private_pem = rsa.exportKey()
with open('ghost-private.pem', 'w') as f:
    f.write(private_pem.decode())

public_pem = rsa.publickey().exportKey()
with open('ghost-public.pem', 'w') as f:
    f.write(public_pem.decode())


s=open('document1' , "r",encoding='utf-8').read()
with open('ghost-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(str(s).encode()))
    #print(cipher_text)
    with open(bytes.decode(base64.b64encode('document1'.encode('utf-8'))), 'w') as file:
        file.write(cipher_text.decode())

s=open('document2' , "r",encoding='utf-8').read()
with open('ghost-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(str(s).encode()))
    #print(cipher_text)
    with open(bytes.decode(base64.b64encode('document2'.encode('utf-8'))), 'w') as file:
        file.write(cipher_text.decode())

s=open('document3' , "r",encoding='utf-8').read()
with open('ghost-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(str(s).encode()))
    #print(cipher_text)
    with open(bytes.decode(base64.b64encode('document3'.encode('utf-8'))), 'w') as file:
        file.write(cipher_text.decode())

s=open('document4' , "r",encoding='utf-8').read()
with open('ghost-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(str(s).encode()))
    #print(cipher_text)
    with open(bytes.decode(base64.b64encode('document4'.encode('utf-8'))), 'w') as file:
        file.write(cipher_text.decode())

s=open('document5' , "r",encoding='utf-8').read()
with open('ghost-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(str(s).encode()))
    #print(cipher_text)
    with open(bytes.decode(base64.b64encode('document5'.encode('utf-8'))), 'w') as file:
        file.write(cipher_text.decode())

s=open('document6' , "r",encoding='utf-8').read()
with open('ghost-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(str(s).encode()))
    #print(cipher_text)
    with open(bytes.decode(base64.b64encode('document6'.encode('utf-8'))), 'w') as file:
        file.write(cipher_text.decode())

