import os
import shutil

dir_1 = "build/exe.win-amd64-3.10/lib/PySide6"

def clean_up():
    print("getting all unnecessary modules to be deleted...")
    unecessary_modules = []
    with open("unnecessary_modules.txt", "r") as f:
        content = f.readlines()
        unecessary_modules = [x.strip() for x in content]
    print("done\n")
    
    print("getting all unnecessary folders to be deleted...")
    unecessary_folders = []
    with open("unnecessary_folders.txt", "r") as f:
        content = f.readlines()
        unecessary_folders = [x.strip() for x in content]
    print("done\n")
    
    print("deleting all unnecessary modules...")
    for file_name in os.listdir(dir_1):
            if os.path.isfile(os.path.join(dir_1, file_name)):
                if file_name in unecessary_modules:
                    os.remove(os.path.join(dir_1, file_name))
    print("done\n")
    
    print("deleting all unnecessary modules...")
    for folder_name in os.listdir(dir_1):
            if os.path.isdir(os.path.join(dir_1, folder_name)):
                if folder_name in unecessary_folders:
                    shutil.rmtree(os.path.join(dir_1, folder_name))
    print("done\n")
    
    print("clean up complete")
    
    
        
if __name__ == '__main__':
    clean_up()
