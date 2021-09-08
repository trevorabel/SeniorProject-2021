# DES encryption method in a python script to be passed to JavaFx main class
#
# Sources
# Storing, loading, and creating keys in python: www.devaq.io/encrypt-decrypt-data-python
#
#
#
import cryptography
from cryptography.fernet import Fernet

# methods for genereating keys, storing keys, and retrieving keys

def gen_key():
    # generate the key needed for DES encryption and decryption (symmetric key)
    key = Fernet.generate_key()
    with open('deskey.key', 'wb') as file:
        file.write(key)

print(0)