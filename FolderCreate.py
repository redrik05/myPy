import os


def folder_create(arg_parent_dir_path, arg_new_dir_name, arg_overwrite):
    new_path = os.path.join(arg_parent_dir_path, arg_new_dir_name)
    if os.path.exists(new_path) != arg_overwrite:
        os.mkdir(new_path)
    else:
        os.rename(new_path, new_path)


parent_dir_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate'
new_dir_name = r'NewDirectory333'
overwrite = True

folder_create(parent_dir_path, new_dir_name, overwrite)
