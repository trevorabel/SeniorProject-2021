# Caesarean encryption method in a python script to be passed to JavaFx main class
#
# Sources:
# Taking user input in python: www.geeksforgeeks.org/taking-input-in-python
#

userInput = int(input("Please enter the shift key for this cipher: "))
userInput2 = input("Please enter a phrase for the cipher: ")

# Encryption below
def encrypt(text, s):
    encryptedText = ""
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            encryptedText += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            encryptedText += chr((ord(char) + s - 97) % 26 + 97)
        else:
            encryptedText += text[i]
    
    return encryptedText

def decrypt(text, s):
    decryptedText = ""
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            decryptedText += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            decryptedText += chr((ord(char) - s - 97) % 26 + 97)
        else:
            decryptedText += text[i]
    
    return decryptedText
    
# testing to ensure that the encryption works properly
#print ("Plain text: " + userInput2)
#print ("Shift key: " + str(userInput))
#encrypted = encrypt(userInput2,userInput)
#print ("Cipher: " + encrypted)
#print ("Decrypted: " + decrypt(encrypted, userInput))