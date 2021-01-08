prompt = "Enter a key (alpha string) \n > "

def encrypt(message, key):
    encrypted = ""
    for i in range(0,len(message)):
        keyLetter = ord(key[i%len(key)])
        encrypted += (chr((ord(message[i].lower())-97+(keyLetter-97))%26+97))
    return encrypted

def decrypt(encrypted, key):
    decrypted = ""
    for i in range(0,len(encrypted)):
        keyLetter = ord(key[i%len(key)])
        decrypted += (chr((ord(encrypted[i].lower())-97-(keyLetter-97))%26+97))
    return decrypted