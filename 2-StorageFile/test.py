import json
from base64 import b64encode
from base64 import b64decode
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

keyword = input("Enter a Filename :")
data = (keyword[:-4]).encode('utf-8')

key = pad(b'secret', 16)

cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
ct_bytes = cipher.encrypt(pad(data, AES.block_size))
L1 = ct_bytes[:8]
hash_object1 = SHA256.new(L1+b'secret')
hashkey = hash_object1.digest()

EncryptedFileName=open("./data/EncryptedFile/EncryptedFileName.txt","r")
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
        Un_filename=keyword
        Un_file=open(Un_filename,"a+")

        file=open("./data/EncryptedFile/"+t[:-1],"r")
        file_data=file.read()

        Un_file.write(b64decode(file_data).decode('utf-8'))
        print(b64decode(file_data).decode('utf-8'))
        Un_file.close()
        file.close()
        
        break
