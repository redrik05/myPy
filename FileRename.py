import os


def file_rename(arg_file_path, arg_new_file_name, arg_overwrite):
    dir_path = os.path.dirname(arg_file_path)
    new_path = os.path.join(dir_path, arg_new_file_name)
    if os.path.exists(new_path) and not arg_overwrite:
        return
    # код не отработал
    # тут ты использовал переменную 'file_path', которая определена снаружи функции.
    # Внутри функции следовало использовать 'arg_file_path'
    os.rename(file_path, x)


# Попробуй библиотеку pathlib. Она сделана по концепциям ООП и намного круче либы 'os'

# from pathlib import Path

# def file_rename_pathlib(arg_file_path, arg_new_file_name, arg_overwrite):
#     arg_file_path = Path(arg_file_path)
#     dir_path = arg_file_path.parent
#     new_path = dir_path.joinpath(arg_new_file_name)
#     if new_path.is_file() and not arg_overwrite:
#         return
#     arg_file_path.rename(Path(new_path))

file_path = r'C:\Users\Багаудин\Desktop\Action\FileCreate\333.txt'
new_file_name = r'yy3.txt'
overwrite = True

file_rename(file_path, new_file_name, overwrite)
