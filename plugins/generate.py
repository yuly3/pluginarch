receive_topic = 'analyze'
send_topic = 'generate'


class Generate:
    def __init__(self):
        self.sentence: str = 'generate'
    
    def generate(self) -> str:
        return self.sentence


def listen(arg: str, write_func):
    print('received from ' + arg)
    generater = Generate()
    write_func(send_topic, generater.generate())
    print('send to ' + send_topic)
