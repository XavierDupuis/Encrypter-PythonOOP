prompt = "Enter a key (0-26) \n > "

def encrypt(message, key):
    encrypted = ""
    for i in message:
        encrypted += (chr((ord(i.lower())-97+int(key))%26+97))
    return encrypted

def decrypt(encrypted, key):
    decrypted = ""
    for i in encrypted:
        decrypted += (chr((ord(i.lower())-97-int(key))%26+97))
    return decrypted

