import os
import numpy as np
from PIL import Image
from tqdm import tqdm
X_array = np.empty(shape=(100, 256, 256, 3))
mask_array = np.empty(shape=(100, 256, 256, 3))
for i, filename in tqdm(enumerate(os.listdir("IMAGES")), desc="Loading images"):
    img = Image.open("IMAGES/" + filename).convert("RGB")
    img = img.resize((256, 256))
    np_img = np.array(img)
    if "mask" in filename:
        mask_array[i // 2] = np_img
    else:
        X_array[i // 2] = np_img
print(X_array.shape)
print(mask_array.shape)
np.save("images.npy", X_array)
np.save("masks.npy", mask_array)
    