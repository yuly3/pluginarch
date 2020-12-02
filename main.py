import glob
import importlib

from pubsub import pub


def write_to_file(send_topic, message):
    with open('./result.txt', mode='w') as file:
        file.write(send_topic + '\n' + message)


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
    
    pub.sendMessage(topicName='start', arg='start', write_func=write_to_file)
    for _ in range(len(modules)):
        with open('./result.txt', mode='r') as file:
            send_topic = file.readline().rstrip()
            message = file.read()
            if send_topic == 'speak':
                pub.sendMessage(topicName=send_topic, arg=message)
            else:
                pub.sendMessage(topicName=send_topic, arg=message, write_func=write_to_file)


if __name__ == '__main__':
    main()
