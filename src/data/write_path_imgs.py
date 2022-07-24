import os


def write_path(path):
    folders = os.listdir(path)
    for folder_name in folders:
        if os.path.isdir(folder):
            train_path = path + folder_name + "/train_" + folder_name + ".txt"
            train_path_folder = path + folder_name + "/images"  + "/train/"
            valid_path = path + folder_name + "/valid_" + folder_name + ".txt"
            valid_path_folder = path + folder_name + "/images" + "/valid/"
            print(train_path)
            with open(train_path, 'w') as f:
                files = os.listdir(train_path_folder)
                for file in files:
                  f.write(train_path_folder + file + "\n")

            with open(valid_path, 'w') as f:
                files = os.listdir(valid_path_folder)
                for file in files:
                  f.write(valid_path_folder + file + "\n")


if __name__ == '__main__':
    path = r"F:\Projects\Levanova\dronedetect\data\raw"
    write_path(path)