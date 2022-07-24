import os
import glob
import shutil


def custom_train_valid_split(path, threshold=0.25):
    img_files = os.listdir(path + "images/")
    #  print(img_files)
    num_files = len(img_files)
    count_valid = round(num_files * threshold)
    k = 0
    for file in img_files:
        if file == "valid" or file == "train":
            continue
        file_name = file[:-4]
        print(file_name)
        if k < count_valid:
            shutil.move(path + "images/" + file_name + ".jpg", path + "images/" + "valid/" + file_name + ".jpg")
            shutil.move(path + "labels/" + file_name + ".txt", path + "labels/" + "valid/" + file_name + ".txt")
            k += 1
        else:
            shutil.move(path + "images/" + file_name + ".jpg", path + "images/" + "train/" + file_name + ".jpg")
            shutil.move(path + "labels/" + file_name + ".txt", path + "labels/" + "train/" + file_name + ".txt")

    print("Done")


if __name__ == '__main__':
    from_path = r"F:\Projects\Levanova\dronedetect\data\raw"
    to_path = "F:\Projects\Levanova\dronedetect\data\processed"
    move_from_folder_to_other_folder(from_path, to_path)
