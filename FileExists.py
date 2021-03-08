import os


def file_exists(arg_path_file):
    x = os.path.exists(arg_path_file)
    return x
    # По техническому заданию экшен должен возвращать значение.
    # А не выводить его на печать
    # Пример:
    # def foo(bar):
    #     foobar = isinstance(bar, bool)
    #     return foobar


file_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate\123.txt'

file_exists(file_path)
