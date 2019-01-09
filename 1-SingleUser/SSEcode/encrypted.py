import json
import pandas as pd
from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

file=pd.read_table("data.csv",sep=",")
key=pad(b'secret',16)
for passenger_index, passenger in file.iterrows():
    strdata = passenger['date']
    data = strdata.encode('utf-8')
    print(data)
    cipher = AES.new(key, AES.MODE_CBC, pad(b'0', AES.block_size))
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
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
    trapdoor = b64encode(c).decode('utf-8')
    passenger['date']=trapdoor
    file.update(pd.Series(trapdoor, name="date", index=[passenger_index]))
    temp1=passenger['reviewer_id']
    entemp1=b64encode(str(temp1).encode('utf-8'))
    temp2=passenger['reviewer_name']
    entemp2=b64encode(temp2.encode('utf-8'))    
    temp3=passenger['comments']
    entemp3=b64encode(str(temp3).encode('utf-8'))
    file.loc[passenger_index]=[trapdoor,entemp1,entemp2,entemp3]
    #print(file.loc[passenger_index])
file.to_csv("test.csv",index=0)
