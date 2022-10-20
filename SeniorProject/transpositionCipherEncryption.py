import pyperclip

userInput = (input("Please enter the message for this cipher: "))
userInput2 = int(input("Please enter the shift key for this cipher: "))

def encrypt(key,message):
    ciphertext = [''] * key

    for col in range(key):
        currentLetter = col
        while currentLetter < len(message):
            ciphertext[col] += message[currentLetter]
            currentLetter += key
    return ''.join(ciphertext)

# testing to ensure the encryption works properly
# ciphertext = encrypt(userInput2, userInput)

# print("Cipher text is: ")
# print(ciphertext)