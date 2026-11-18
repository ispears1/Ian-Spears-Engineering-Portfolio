Cipher =  {'A': 'Z', 'B': 'A', 'C': 'V',  'D': 'K',  'E': 'F',  'F': 'D',  'G': 'X',  'H': 'C',  'I': 'G',  'J': 'E',  'K': 'W',  'L': 'L',  'M': 'I',  'N': 'P', 'O': 'Y',  'P': 'H', 'Q': 'R', 'R': 'B',  'S': 'N',  'T': 'S',  'U': 'J',  'V': 'M',  'W': 'O',  'X': 'Q',  'Y': 'U',  'Z': 'T'}

def encrypt(message, code):
    encryptedMessage =""
    for i in range(len(message)):
        letter = message[i:i+1]
        letter = letter.capitalize()
        if(letter in code):
            encryptedMessage = encryptedMessage + code[letter]
        else:
            encryptedMessage = encryptedMessage + letter
    return encryptedMessage
        
def decrypt(message, code):
    decryptedMessage = ""
    for i in range(len(message)):
        letter = message[i:i+1]
        letter = letter.capitalize()
        if(letter in code):
            for key, value in code.items():
                if (value == letter):
                    decryptedMessage = decryptedMessage + key
        else:
            decryptedMessage = decryptedMessage + letter
    return decryptedMessage.lower()

if __name__ == "__main__":
    secret = input("Enter message to be encrypted: ")
    print(encrypt(secret, Cipher))
    unravel = input("Enter message to be decoded: ")
    print(decrypt(unravel, Cipher))
