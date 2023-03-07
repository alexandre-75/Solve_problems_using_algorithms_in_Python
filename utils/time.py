from datetime import datetime

class Time():
    def __init__(self):
        pass

    def time(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        return time
