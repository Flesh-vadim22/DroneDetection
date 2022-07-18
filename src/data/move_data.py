import os
import glob
import shutil


def move_imgs_to_folder(from_path, to_path, threshold=0.25):
    folders_data = os.listdir(from_path)
  #  for folder in folders_data
    folder = folders_data[5]
    if os.path.isdir(from_path + r'\\' + folder):
        imgs_path = from_path + r'\\' + folder
        os.chdir(imgs_path)
        imgs = glob.glob("*.jpg")
        labels = glob.glob("*.txt")
        cout_files = len(imgs)
        print(cout_files)
        cout_valid = round(cout_files * threshold)
        print(cout_valid)
        k = 0
        for item in range(0, cout_files):
            if imgs[item] == "ch01_20200605113709-part 00000-frame 00023008.jpg":
                continue
            if k <=cout_valid:
                shutil.copy(imgs_path + r"\\" + imgs[item], to_path + r"\images\valid")
                shutil.copy(imgs_path + r"\\" + labels[item], to_path + r"\labels\yolo_format\valid")
                k+=1
            else:
                shutil.copy(imgs_path + r"\\" + imgs[item], to_path + r"\images\train")
                shutil.copy(imgs_path + r"\\" + labels[item], to_path + r"\labels\yolo_format\train")


if __name__ == '__main__':
    threshold = 0.25
    from_path = r"F:\Projects\леванова\dronedetect\data\raw"
    to_path = "F:\Projects\леванова\dronedetect\data\processed"
    move_imgs_to_folder(from_path, to_path, threshold)
