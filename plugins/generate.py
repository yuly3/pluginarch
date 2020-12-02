receive_topic = 'analyze'
send_topic = 'generate'


class Generate:
    def __init__(self):
        self.sentence = 'generate'
    
    def generate(self):
        return self.sentence


def listen(arg, write_func):
    print('received from ' + arg)
    generater = Generate()
    write_func(send_topic, generater.generate())
    print('send to ' + send_topic)
