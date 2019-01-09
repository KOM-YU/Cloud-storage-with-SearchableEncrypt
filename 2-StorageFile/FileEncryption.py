import json
import pandas as pd
from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

key = pad(b'secret', 16)

encryptedfileindex=open("EncryptedFileName.txt","a+")

#document1.txt
file1=open("document1.txt","r")
keywords1="document1"
data1 = keywords1.encode('utf-8')
cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
ct_bytes = cipher.encrypt(pad(data1, AES.block_size))
L = ct_bytes[:8]
hash_object1 = SHA256.new(L+b'secret')
hashkey = hash_object1.digest()

prs = get_random_bytes(8)
hash_object = SHA256.new(prs+hashkey)
hash = hash_object.digest()

t = prs + hash[:8]

c = bytearray(len(ct_bytes))
for i in range(len(ct_bytes)):
    c[i] = ct_bytes[i] ^ t[i]

newfilename1 = b64encode(c).decode('utf-8')+".txt"
encryptedfileindex.write(newfilename1+"\n")

encryptedfile1=open(newfilename1,"a+")
filedata1=file1.read()
encryptedfile1.write(b64encode(filedata1.encode('utf-8')).decode('utf-8'))

encryptedfile1.close()
file1.close()

#document2.txt
file2=open("document2.txt","r")
keywords2="document2"
data2 = keywords2.encode('utf-8')
cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
ct_bytes = cipher.encrypt(pad(data2, AES.block_size))
L = ct_bytes[:8]
hash_object1 = SHA256.new(L+b'secret')
hashkey = hash_object1.digest()

prs = get_random_bytes(8)
hash_object = SHA256.new(prs+hashkey)
hash = hash_object.digest()

t = prs + hash[:8]

c = bytearray(len(ct_bytes))
for i in range(len(ct_bytes)):
    c[i] = ct_bytes[i] ^ t[i]

newfilename2 = b64encode(c).decode('utf-8')+".txt"
encryptedfileindex.write(newfilename2+"\n")

encryptedfile2=open(newfilename2,"a+")
filedata2=file2.read()
encryptedfile2.write(b64encode(filedata2.encode('utf-8')).decode('utf-8'))

encryptedfile2.close()
file2.close()

#document3.txt
file3=open("document3.txt","r")
keywords3="document3"
data3 = keywords3.encode('utf-8')
cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
ct_bytes = cipher.encrypt(pad(data3, AES.block_size))
L = ct_bytes[:8]
hash_object1 = SHA256.new(L+b'secret')
hashkey = hash_object1.digest()

prs = get_random_bytes(8)
hash_object = SHA256.new(prs+hashkey)
hash = hash_object.digest()

t = prs + hash[:8]

c = bytearray(len(ct_bytes))
for i in range(len(ct_bytes)):
    c[i] = ct_bytes[i] ^ t[i]

newfilename3 = b64encode(c).decode('utf-8')+".txt"
encryptedfileindex.write(newfilename3+"\n")

encryptedfile3=open(newfilename3,"a+")
filedata3=file3.read()
encryptedfile3.write(b64encode(filedata3.encode('utf-8')).decode('utf-8'))

encryptedfile3.close()
file3.close()

#document4.txt
file4=open("document4.txt","r")
keywords4="document4"
data4 = keywords4.encode('utf-8')
cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
ct_bytes = cipher.encrypt(pad(data4, AES.block_size))
L = ct_bytes[:8]
hash_object1 = SHA256.new(L+b'secret')
hashkey = hash_object1.digest()

prs = get_random_bytes(8)
hash_object = SHA256.new(prs+hashkey)
hash = hash_object.digest()

t = prs + hash[:8]

c = bytearray(len(ct_bytes))
for i in range(len(ct_bytes)):
    c[i] = ct_bytes[i] ^ t[i]

newfilename4 = b64encode(c).decode('utf-8')+".txt"
encryptedfileindex.write(newfilename4+"\n")

encryptedfile4=open(newfilename4,"a+")
filedata4=file4.read()
encryptedfile4.write(b64encode(filedata4.encode('utf-8')).decode('utf-8'))

encryptedfile4.close()
file4.close()

#document5.txt
file5=open("document5.txt","r")
keywords5="document5"
data5 = keywords5.encode('utf-8')
cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
ct_bytes = cipher.encrypt(pad(data5, AES.block_size))
L = ct_bytes[:8]
hash_object1 = SHA256.new(L+b'secret')
hashkey = hash_object1.digest()

prs = get_random_bytes(8)
hash_object = SHA256.new(prs+hashkey)
hash = hash_object.digest()

t = prs + hash[:8]

c = bytearray(len(ct_bytes))
for i in range(len(ct_bytes)):
    c[i] = ct_bytes[i] ^ t[i]

newfilename5 = b64encode(c).decode('utf-8')+".txt"
encryptedfileindex.write(newfilename5+"\n")

encryptedfile5=open(newfilename5,"a+")
filedata5=file5.read()
encryptedfile5.write(b64encode(filedata5.encode('utf-8')).decode('utf-8'))

encryptedfile5.close()
file5.close()

#document6.txt
file6=open("document6.txt","r")
keywords6="document6"
data6 = keywords6.encode('utf-8')
cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
ct_bytes = cipher.encrypt(pad(data6, AES.block_size))
L = ct_bytes[:8]
hash_object1 = SHA256.new(L+b'secret')
hashkey = hash_object1.digest()

prs = get_random_bytes(8)
hash_object = SHA256.new(prs+hashkey)
hash = hash_object.digest()

t = prs + hash[:8]

c = bytearray(len(ct_bytes))
for i in range(len(ct_bytes)):
    c[i] = ct_bytes[i] ^ t[i]

newfilename6 = b64encode(c).decode('utf-8')+".txt"
encryptedfileindex.write(newfilename6+"\n")

encryptedfile6=open(newfilename6,"a+")
filedata6=file6.read()
encryptedfile6.write(b64encode(filedata6.encode('utf-8')).decode('utf-8'))

encryptedfile6.close()
file6.close()

encryptedfileindex.close()
