import glob
import importlib


def main():
    file_paths = glob.glob('./plugins/*.py')
    for file_path in file_paths:
        module = importlib.import_module('plugins.' + file_path[10:-3])
        plugin_class = module.plugin(5)
        plugin_class.output()


if __name__ == '__main__':
    main()
