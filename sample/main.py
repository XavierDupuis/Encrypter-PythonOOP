from encryptions import *
from message import *

if __name__ == "__main__":
    message = message.Message("Xavier")
    y = input()
    encrypted=caesar.encryptCaesar(message.message_, y)
    print(encrypted)
    print(caesar.decryptCaesar(encrypted, y))
    input()
