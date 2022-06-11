class Logger:
    def __init__(self):
        self.messages = []

    def log(self, info):
        print(info)
        self.messages.append(info)

    def flush(self):
        self.messages = []

logger = Logger()

