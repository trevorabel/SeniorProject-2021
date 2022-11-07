# RC2 encryption method in a python script to be passed to JavaFx main class
#
# Sources
# RC2: https://pycryptodome.readthedocs.io/en/latest/src/cipher/arc2.html
# Modern Modes of Operation for Symmetric Block Ciphers: https://pycryptodome.readthedocs.io/en/latest/src/cipher/modern.html#eax-mode

from Crypto.Cipher import ARC2
from Crypto.Random import get_random_bytes

# methods for genereating keys, storing keys, and retrieving keys

def gen_key():
    # generate the key needed for RC2 encryption and decryption (symmetric key)
    key = get_random_bytes(16)
    with open("rc2Secretkey.key", "wb") as file:
        file.write(key)

def load_key():
    return open("rc2Secretkey.key", "rb").read()

def encrypt_message(message,key):
    # # Steps for encryption:
    #  1. Create Cipher instance with RC2
    #  2. Store cipher instance into a nonce to be recalled for decryption later
    #  3. Write out stored cipher(nonce) to a file to be read in for decryption
    #  4. Perform encryption while creating variables for the the encryption and tag
    #  5. Write out Encryption and Tag variables to a file to be recalled for decryption of stored message
    # #

    RC2cipher = ARC2.new(key, ARC2.MODE_EAX)
    cipherStore = RC2cipher.nonce

    # writing cipherStore/nonce out to a file to be pulled for decryption
    with open("rc2CipherStore_nonce.txt", "wb") as file:
        file.write(cipherStore)
        print("Export of variable cipherStore aka nonce complete. Proceeding with encryption.")

    encrpyted, tag = RC2cipher.encrypt_and_digest(message)

    # writing out created variable tag needed for validity checking while decryption to ensure authenticity of the message
    with open("rc2EncryptedTag.txt", "wb") as file:
        file.write(tag)
        print("Export of variable tag aka RC2 encrypted text identifier for verification complete. Proceeding with writing out Encrypted message. Returning to Menu.")

    # writing encryption out to a file to be stored for decryption
    with open("rc2Encrypted.txt", "wb") as file:
        file.write(encrpyted)
        print("Export of variable encrypted aka RC2 encrypted text complete. Finished with encryption process. Returning to Menu.")

    # # Test block below to return within the class to test the functionality of the RC2 class
    # # return encrypted message to compare against the decryption to prove its encryption then decryption back to the correct plaintext.
    # return encrpyted, cipherStore, tag

def decrypt_message(message,key,cipherStore,tag):
    # # Steps for encryption
    #  1. Recreate Cipher instance for RC2 with the key, RC2.MODE_EAX from above, and the cipherStore/Nonce from encryption
    #  2. Perform decryption
    #  3. Create If statement to check that the tag from the encryption mathces the now decrypted message
    #     a. If the tag matches then write out the decrypted contents to a file to be stored
    #     b. If the tag does not match return a statement that there is an error with the decryption.
    #  4. Write out Encryption and Tag variables to a file to be recalled for decryption of stored message
    # #
    decryptCipher = ARC2.new(key, ARC2.MODE_EAX, nonce=cipherStore)
    decrypt = decryptCipher.decrypt(message)

    # try statement to see if the decrypted message matches the contents of the original text
    try:
        #condition to verify the tag from the encrypted message
        decryptCipher.verify(tag)
        
        # writing encryption out to a file to be stored for decryption
        with open("rc2Decrypted.txt", "wb") as file:
            file.write(decrypt)
            print("Tag matches original tag, export of variable decrypt aka RC2 decrypted text complete. Finished with decryption process. Returning to Menu.")

        # # Test block below to return within the class to test the functionality of the RC2 class
        # #return plaintext/decrypted message if true
        # return decrypt.decode('ascii')
    except:
        print("Error in decryption original text and decrypted text do not match!")
        return False

# # Test code for ensuring that the functionality of this code works.
# # Testing the pass through capabilities of the RC2 decryption method and compatibility of saved files for Key, Encrypted message, CipherStore/Nonce, and Tag
# msg = "hello world"
# gen_key()
# encrypt_message(msg,key=load_key())
# print("Encryption complete!")
# decrypt_message(message=open("rc2Encrypted.txt", "rb").read(),key=load_key(),cipherStore=open("rc2CipherStore_nonce.txt", "rb").read(), tag=open("rc2EncryptedTag.txt", "rb").read())
# print("Decryption complete!")
# 
# # Testing the pass through capabilities of the RC2 encryption and decrpyion method and compatibility of saved files for Message, Key, Encrypted message, CipherStore/Nonce, and Tag# 
# msg=open("test.txt", "rb").read()
# gen_key()
# encrypt_message(msg,key=load_key())
# print("Encryption complete!")
# decrypt_message(message=open("rc2Encrypted.txt", "rb").read(),key=load_key(),cipherStore=open("rc2CipherStore_nonce.txt", "rb").read(), tag=open("rc2EncryptedTag.txt", "rb").read())
# print("Decryption complete!")