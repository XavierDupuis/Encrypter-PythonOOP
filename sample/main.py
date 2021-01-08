from encryptions import *
from message import *

def testEncryption(method, message):
    valid = False
    while not valid:
        try:
            y = input(method.prompt)
            encrypted=method.encrypt(message.message_, y)
            valid = True
        except ValueError as ex:
           print(ex) 
    print("Encrypted : " + encrypted)
    print("Decrypted : " + method.decrypt(encrypted, y))

if __name__ == "__main__":
    message = message.Message("Xavier")
    testEncryption(caesar, message)
    testEncryption(caesar, message)
    testEncryption(caesar, message)
    testEncryption(vigenere, message)
    input("\nEND\n")

