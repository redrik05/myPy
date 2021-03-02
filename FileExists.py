import os


def file_exists(arg_path_file):
    x = os.path.exists(arg_path_file)
    print(x)


file_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate\123.txt'

file_exists(file_path)
