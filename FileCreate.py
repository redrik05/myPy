import os


def file_create(arg_file_path, arg_file_name, arg_overwrite):
    new_file_path = os.path.join(arg_file_path, arg_file_name)
    if os.path.exists(new_file_path) and not arg_overwrite:
        return
    new_file = open(new_file_path, 'w')
    new_file.close()


file_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate'
file_name = r'123.txt'
overwrite = True

# Код не отработал. Забыл переименовать переменные?
file_create(_file_path, _file_name, _overwrite)
