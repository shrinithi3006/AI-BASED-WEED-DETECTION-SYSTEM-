import os
import random
import shutil

labels_path = r"C:\Users\Asus\OneDrive\Desktop\Agri_Imageprocessing\WEED_DETECTION\dataset\labels"
images_path = r"C:\Users\Asus\OneDrive\Desktop\Agri_Imageprocessing\WEED_DETECTION\dataset\images"

target_ratio = 1.3   # weed : crop

crop_files = []
weed_files = []

for root, dirs, files in os.walk(labels_path):
    for file in files:
        if file.endswith(".txt"):

            path = os.path.join(root, file)

            with open(path) as f:
                lines = f.readlines()

            classes = [int(line.split()[0]) for line in lines]

            if 1 in classes:
                weed_files.append(file.replace(".txt",".jpg"))
            elif 0 in classes:
                crop_files.append(file.replace(".txt",".jpg"))

crop_count = len(crop_files)
weed_count = len(weed_files)

print("Original Crop:",crop_count)
print("Original Weed:",weed_count)

target_crop = int(weed_count / target_ratio)

remove_crop = crop_count - target_crop

print("Crop images to remove:",remove_crop)

if remove_crop > 0:

    remove_list = random.sample(crop_files, remove_crop)

    for img in remove_list:

        src = os.path.join(images_path,img)
        dst = os.path.join(images_path,"removed_"+img)

        if os.path.exists(src):
            shutil.move(src,dst)

print("Dataset balanced!")