import os


def folder_delete(arg_dir_path, arg_overwrite):
    if len(os.listdir(arg_dir_path)) != 0:
        print('Папка не пуста')
        return
    if os.path.exists(dir_path) and not arg_overwrite:
        return
    os.rmdir(arg_dir_path)


dir_path = r'C:\Users\Багаудин\Desktop\Action\FileCreateNew\NewDir'
overwrite = True

# Код не отработал. Забыл переименовать переменные?
folder_delete(_dir_path, _overwrite)

# Требуется доработка
# По тех. заданию требовалось удалить директорию, независимо от того, пуста она или нет
