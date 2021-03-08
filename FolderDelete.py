import os


def folder_delete(arg_dir_path, arg_overwrite):
    if os.path.exists(dir_path) != arg_overwrite:
        return
    os.rmdir(arg_dir_path)


dir_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate\NewDirectory333'
overwrite = True

folder_delete(dir_path, overwrite)
