receive_topic = 'generate'
send_topic = 'speak'


class Speak:
    def __init__(self):
        self.can_speak = 'speak'
    
    def speak(self):
        return self.can_speak


def listen(arg):
    print('received from ' + arg)
    speaker = Speak()
    with open('./result.txt', mode='w') as file:
        file.write(send_topic + '\n' + speaker.speak())
    print('send to ' + send_topic)
