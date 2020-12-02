import glob
import importlib

from pubsub import pub


def listen(arg):
    print('received from ' + arg)


def main():
    file_paths = glob.glob('./plugins/*.py')
    modules = []
    for file_path in file_paths:
        module = importlib.import_module('plugins.' + file_path[10:-3])
        modules.append(module)
        pub.subscribe(module.listen, module.receive_topic)
    pub.subscribe(listen, 'speak')
    
    pub.sendMessage(topicName='start', arg='start')
    for _ in range(len(modules)):
        with open('./result.txt', mode='r') as file:
            send_topic = file.readline().rstrip()
            message = file.read()
            print(message)
            pub.sendMessage(topicName=send_topic, arg=message)


if __name__ == '__main__':
    main()
