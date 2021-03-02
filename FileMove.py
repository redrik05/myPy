import os
import shutil


def file_move(arg_source_path, arg_dest_dir_path, arg_new_file_name, arg_overwrite):
    new_file_path = os.path.join(arg_dest_dir_path, arg_new_file_name)
    if os.path.exists(new_file_path) and not arg_overwrite:
        return
    shutil.move(arg_source_path, new_file_path)


source_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate\123.txt'
dest_dir_path = r'C:\Users\Багаудин\Desktop\Action\FileCreateNew'
new_file_name = r'444.txt'
overwrite = True

file_move(source_path, dest_dir_path, new_file_name, overwrite)
