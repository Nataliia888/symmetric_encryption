# symmetric_encryption

#library: cryptography: pip install cryptography
from cryptography.fernet import Fernet
#Fernet - is authenticated cryptography which doesn’t allow to read or modify the file without a “key”.


'''1. #Generate Key
key = Fernet.generate_key()
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


