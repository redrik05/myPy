import os
import shutil


def folder_copy(arg_folder_path, arg_destination_path, arg_new_directory_name, arg_overwrite):
    new_path = os.path.join(arg_destination_path, arg_new_directory_name)
    if os.path.exists(new_path) and not arg_overwrite:
        return
    shutil.copytree(arg_folder_path, new_path)


folder_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate'
destination_path = r'C:\Users\Багаудин\Desktop\Action\FileCreateNew'
new_directory_name = r'NewDir13355'
overwrite = True

folder_copy(folder_path, destination_path, new_directory_name, overwrite)
