import os
import shutil
import difflib

def ask_what_to_do(quote_file_path, backup_file_path, diff):
    while True:
        choice = input('[S]ee changes, [a]ccept changes or [r]estore backup: ').lower()
        match choice:
            case 's':
                print(diff)
            case 'a':
                os.remove(backup_file_path)
                shutil.copyfile(quote_file_path, backup_file_path)
                break
            case 'r':
                os.remove(quote_file_path)
                shutil.copy(backup_file_path, quote_file_path)
                break
            case _:
                'wrong option, try again'

def check_file_integrity(quotes_dir_path):
    if not os.path.isdir(os.path.join(quotes_dir_path, '.backup')):
        os.mkdir(os.path.join(quotes_dir_path, '.backup'))

    quotes_files_paths = sorted([os.path.join(quotes_dir_path, xfile) for xfile in os.listdir(quotes_dir_path) if xfile.endswith('.md')])
    for quote_file_path in quotes_files_paths:
        backup_file_path = os.path.join(quotes_dir_path, '.backup', os.path.basename(quote_file_path))
        if not os.path.isfile(backup_file_path):
            shutil.copyfile(quote_file_path, backup_file_path)
            continue
        diff = ("").join(
            difflib.unified_diff(open(quote_file_path).readlines(), open(backup_file_path).readlines(), n=0, fromfile='main', tofile='backup')
        )
        if diff:
            print(f'File {os.path.basename(quote_file_path)} has been changed')
            ask_what_to_do(quote_file_path, backup_file_path, diff)
