import os
import shutil
import time


def get_file_age(path):
    ctime = os.stat(path).st_ctime
    return ctime


def main():
    path = "D:\\NEWfolder"

    time_range = 60  # Minutes
    seconds = time.time() - (time_range * 60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            print(root_folder, folders, files)
            print(folders)
            for file_name in files:
                file_path = os.path.join(root_folder, file_name)
                if seconds <= get_file_age(file_path):
                    os.remove(file_path)

            for folder_name in folders:
                folder_path = os.path.join(root_folder, folder_name)
                # print(folder_path)
                if seconds <= get_file_age(folder_path):
                    shutil.rmtree(folder_path)

