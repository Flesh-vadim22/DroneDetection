import glob
import pandas as pd
import numpy as np


path_dir = r"C:\Users\Vadim\Desktop\folders\For myself\Levanova\Drones\drones\data\raw\*"

folders = glob.glob(path_dir)
print(folders[0])
data = []
for fold in range(0, len(folders)):
    files = glob.glob(folders[fold] + "\\" + '*.txt')
    for file in files:
        f = open(file, 'r')
        values = f.readline()
        values = values.split(" ")
        values[4] = values[4].replace("\n", "")
        # print(values[4])
        new_file = file.replace("txt", "jpg")
        name_file = new_file.replace(folders[fold] + '\\', "")
        # print(folders[fold] + '\\')
        # print(new_file)
        # print(name_file)
        # print(values)
        data.append([name_file, new_file, values[1], values[2], values[3], values[4], values[0]])


print(data)
df = pd.DataFrame(np.array(data), columns=["name", "path_img", "x_center", "y_center", "width", "height", "category"])
df.to_csv("train.csv")