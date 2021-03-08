import os


def file_rename(arg_file_path, arg_new_file_name, arg_overwrite):
    dir_path = os.path.dirname(arg_file_path)
    new_path = os.path.join(dir_path, arg_new_file_name)
    if os.path.exists(new_path) and not arg_overwrite:
        return
    os.rename(arg_file_path, new_path)


file_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate\333.txt'
new_file_name = r'y55.txt'
overwrite = True

file_rename(file_path, new_file_name, overwrite)
