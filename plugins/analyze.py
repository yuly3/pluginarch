receive_topic = 'start'
send_topic = 'analyze'


class Analyze:
    def __init__(self):
        self.analysis = 'analyze'
    
    def analyze(self):
        return self.analysis


def listen(arg, write_func):
    print('received from ' + arg)
    analyzer = Analyze()
    write_func(send_topic, analyzer.analyze())
    print('send to ' + send_topic)
