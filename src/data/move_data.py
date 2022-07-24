import os
import glob
import shutil


def sorted_imgs(path):
    files = os.listdir(path)
    for folder_name in files:
        if os.path.isdir(file):
            train_path = path + folder_name + r"\train_" + folder_name + ".txt"
            valid_path = path + folder_name + r"\valid_" + folder_name + ".txt"

            with open(train_path, 'r') as f:
                train_files = f.readlines()
            train_files.sort()
            with open(train_path, 'w') as f:
                for file in train_files:
                    f.write(file)

            with open(valid_path, 'r') as f:
                valid_files = f.readlines()
                valid_files.sort()
                for file in valid_files:
                    f.write(file)

            with open(valid_path, 'w') as f:
                for file in valid_files:
                    f.write(file)


if __name__ == '__main__':
    path = r"F:\Projects\Levanova\dronedetect\data\raw\00_01_52_to_00_01_58\\"
    sorted_imgs(path)
