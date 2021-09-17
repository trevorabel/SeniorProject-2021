# DES encryption method in a python script to be passed to JavaFx main class
#
# Sources
# Storing, loading, and creating keys in python: www.devaq.io/encrypt-decrypt-data-python
#
#
#
from cryptography.fernet import Fernet

# methods for genereating keys, storing keys, and retrieving keys

def gen_key():
    # generate the key needed for DES encryption and decryption (symmetric key)
    key = Fernet.generate_key()
    with open("secretkey.key", "wb") as file:
        file.write(key)

def load_key():
    return open("secretkey.key", "rb").read()

def encrypt_message(message):
    gen_key()

    f = Fernet(load_key())

    message_enc = message.encode()

    encrypted_message = f.encrypt(message_enc)

message = "test message"

print("original string: ", message)
print("enc string: ", encrypt_message(message))