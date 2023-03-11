import os
import shutil

lib_path = os.path.abspath("build/lib/PySide6")
file_path = os.path.abspath("unnecessary_modules.txt")
folder_path = os.path.abspath("unnecessary_folders.txt")

def clean_up():
    print("getting all unnecessary modules to be deleted...")
    unecessary_modules = []
    with open(file_path, "r") as f:
        content = f.readlines()
        unecessary_modules = [x.strip() for x in content]
    print("done\n")
    
    print("getting all unnecessary folders to be deleted...")
    unecessary_folders = []
    with open(folder_path, "r") as f:
        content = f.readlines()
        unecessary_folders = [x.strip() for x in content]
    print("done\n")
    
    print("deleting all unnecessary modules...")
    for file_name in os.listdir(lib_path):
            if os.path.isfile(os.path.join(lib_path, file_name)):
                if file_name in unecessary_modules:
                    os.remove(os.path.join(lib_path, file_name))
    print("done\n")
    
    print("deleting all unnecessary folders...")
    for folder_name in os.listdir(lib_path):
            if os.path.isdir(os.path.join(lib_path, folder_name)):
                if folder_name in unecessary_folders:
                    shutil.rmtree(os.path.join(lib_path, folder_name))
    print("done\n")
    
    print("clean up complete")
    
    
        
if __name__ == '__main__':
    clean_up()
