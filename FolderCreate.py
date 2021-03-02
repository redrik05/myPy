import os
import shutil


def folder_create(arg_parent_dir_path, arg_new_dir_name, arg_overwrite):
    new_path = os.path.join(arg_parent_dir_path, arg_new_dir_name)
    if os.path.exists(new_path) and not arg_overwrite:
        return
    os.mkdir(new_path)


parent_dir_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate'
new_dir_name = r'NewDirectory2'
overwrite = True

folder_create(parent_dir_path, new_dir_name, overwrite)
