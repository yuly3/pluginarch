receive_topic = 'generate'
send_topic = 'speak'


class Speak:
    def __init__(self):
        self.can_speak: str = 'speak'
    
    def speak(self) -> str:
        return self.can_speak


def listen(arg: str, write_func):
    print('received from ' + arg)
    speaker = Speak()
    write_func(send_topic, speaker.speak())
    print('send to ' + send_topic)
