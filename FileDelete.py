import os


def file_delete(arg_file_path):
    os.remove(arg_file_path)
    
    # Тут не нужно использовать pass.
    # pass используют обычно  в качестве заглушки у функции.
    # Например:

    # def foo(bar):
    #     pass


file_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate\111.txt'

file_delete(file_path)
