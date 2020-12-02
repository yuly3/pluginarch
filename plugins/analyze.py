receive_topic = 'start'
send_topic = 'analyze'


class Analyze:
    def __init__(self):
        self.analysis = 'analyze'
    
    def analyze(self):
        return self.analysis


def listen(arg):
    print('received from ' + arg)
    analyzer = Analyze()
    with open('./result.txt', mode='w') as file:
        file.write(send_topic + '\n' + analyzer.analyze())
    print('send to ' + send_topic)
