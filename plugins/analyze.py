receive_topic = 'start'
send_topic = 'analyze'


class Analyze:
    def __init__(self):
        self.analysis: str = 'analyze'
    
    def analyze(self) -> str:
        return self.analysis


def listen(arg: str, write_func) -> None:
    print('received from ' + arg)
    analyzer = Analyze()
    write_func(send_topic, analyzer.analyze())
    print('send to ' + send_topic)
