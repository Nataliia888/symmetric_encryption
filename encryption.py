
#library: cryptography: pip install cryptography
from cryptography.fernet import Fernet
#Fernet - is authenticated cryptography which doesn’t allow to read or modify the file without a “key”.


#1. Generate Key
'''key = Fernet.generate_key()

#w - write; b - binary
with open('mykey.key', 'wb') as mykey:
    mykey.write(key)'''

#2. Encryption

#r - read; b - binary
'''with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)

#We initialize the Fernet object
f = Fernet(key)

with open('PII.csv', 'rb') as original_file:
    original = original_file.read()

#Then we encrypt the data using the Fernet object and store it as encrypted
encrypted = f.encrypt(original)

with open('encrypted_PII.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)'''

#3. Decruption

'''with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

print(key)
#We initialize the Fernet object 
f = Fernet(key)

with open('encrypted_PII.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()
#we decrypt the data using the Fernet object
decrypted = f.decrypt(encrypted)

with open('decrypted_PII.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)'''

'''hashlib is a hashing function that takes variable length
of bytes and converts it into a fixed-length sequence'''
import hashlib

#The function returns a hash of the file passed into it
def get_file_sha(file):
    # Initializing the sha256() method
    m = hashlib.sha256()
    # loop till the end of the file
    chunk = 0
    while chunk != b'':
        # we can read only 1024 bytes at a time
        chunk = file.read(1024)
        m.update(chunk)
        # return the hex representation of SHA-256 digest
        return m.hexdigest()

# open file for reading in binary mode
with open('decrypted_PII.csv', 'rb') as f1, open('PII.csv', 'rb') as f2:
    file1 = get_file_sha(f1)
    file2 = get_file_sha(f2)
    print('file1:', file1)
    print('file2:', file2)
    if file1 != file2:
        print('file is changed')
    else:
        print('file is not changed')


