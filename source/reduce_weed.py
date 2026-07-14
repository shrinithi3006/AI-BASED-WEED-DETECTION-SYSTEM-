import os
import random

label_path = r"C:\Users\Asus\OneDrive\Desktop\Agri_Imageprocessing\WEED_DETECTION\dataset\labels\train"

for file in os.listdir(label_path):
    if file.endswith(".txt"):
        full_path = os.path.join(label_path, file)

        with open(full_path, "r") as f:
            lines = f.readlines()

        new_lines = []

        for line in lines:
            cls = int(line.split()[0])

            if cls == 1:
                # keep all weed
                new_lines.append(line)
            else:
                # keep only some crop (30%)
                if random.random() < 0.3:
                    new_lines.append(line)

        with open(full_path, "w") as f:
            f.writelines(new_lines)

print("✅ Dataset balanced (weed priority)")