import os

label_path = r"C:\Users\Asus\OneDrive\Desktop\Agri_Imageprocessing\WEED_DETECTION\dataset\labels"

crop = 0
weed = 0

for root, dirs, files in os.walk(label_path):

    for file in files:

        if file.endswith(".txt"):

            file_path = os.path.join(root, file)

            with open(file_path, "r") as f:

                for line in f:

                    cls = int(line.split()[0])

                    if cls == 0:
                        crop += 1
                    elif cls == 1:
                        weed += 1

print("Total Crop labels:", crop)
print("Total Weed labels:", weed)