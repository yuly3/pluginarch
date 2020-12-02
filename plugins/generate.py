receive_topic = 'analyze'
send_topic = 'generate'


class Generate:
    def __init__(self):
        self.sentence = 'generate'
    
    def generate(self):
        return self.sentence


def listen(arg):
    print('received from ' + arg)
    generater = Generate()
    with open('./result.txt', mode='w') as file:
        file.write(send_topic + '\n' + generater.generate())
    print('send to ' + send_topic)
