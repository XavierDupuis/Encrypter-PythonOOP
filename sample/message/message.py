class Message:
    message_=''

    def __init__(self, message):
        print("Message CONSTRUCTEUR")
        self.message_=message

    def encrypt(key):
        pass

    def decrypt(key):
        pass

    def __del__(self):
        print("Message DESTRUCTEUR")
        self.message_=''