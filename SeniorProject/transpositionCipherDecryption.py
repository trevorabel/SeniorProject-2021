import pyperclip, math

userInput = (input("Please enter the message used for this encryption: "))
userInput2 = int(input("Please enter the shift key used for this encryption: "))

def decrypt(key,message):
    numCol = math.ceil(len(message) / key)
    numRows = key
    numBoxes = (numCol * numRows) - len(message)
    #Float = float(message)
    regulartext = [''] * numCol
    col = 0
    row = 0

    for symbol in message:
        regulartext[col] += symbol
        col += 1
        if(col == numCol) or (col == numCol -1 and row >= numRows - numBoxes):
            col = 0 
            row += 1 
    return ''.join(regulartext)


# testing to ensure the decryption works properly
#originalText = decrypt(userInput2,userInput)

#print("Original text is: ")
#print(originalText)