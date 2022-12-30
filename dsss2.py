import os
import json
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

directory = "C:/Users/rshru/OneDrive/Desktop/DSSS/Mini_BAGLS_dataset/Mini_BAGLS_dataset"

# Task1: Load 4 random images and corresponding segmentation masks and metadata
random_img = np.random.randint(100, size=4)
fig, axs = plt.subplots(2, 2)

for i, x in enumerate(random_img):
    f_img = os.path.join(directory, str(x) + ".png")
    f_seg = os.path.join(directory, str(x) + "_seg.png")
    f_meta = os.path.join(directory, str(x) + ".meta")
    meta_file = open(f_meta)
    meta_data = json.load(meta_file)
    img = Image.open(f_img)
    seg = Image.open(f_seg)

# Task2: Display img and seg mask overlaid using subplot
    axs[int(np.binary_repr(i, width=2)[0]), int(np.binary_repr(i, width=2)[1])].imshow(img, cmap='gray')
    axs[int(np.binary_repr(i, width=2)[0]), int(np.binary_repr(i, width=2)[1])].imshow(seg, cmap='jet', alpha=0.5)
    axs[int(np.binary_repr(i, width=2)[0]), int(np.binary_repr(i, width=2)[1])].set_title(meta_data['Subject disorder '
                                                                                                    'status'])
plt.show()

#  Task3: RGB to GrayScale
fig, axs = plt.subplots(1, 4)
f_leaves = np.array(Image.open("C:/Users/rshru/OneDrive/Desktop/DSSS/leaves.jpg"))
print(f_leaves)
axs[0].imshow(f_leaves)
axs[0].set_title('Original')
# Lightness Method
f_leaves[:] = np.max(f_leaves, axis=-1, keepdims=True)/2+np.min(f_leaves, axis=-1, keepdims=True)/2
axs[1].imshow(f_leaves)
axs[1].set_title('Lightness')
# Average Method
f_leaves[:] = f_leaves.mean(axis=-1, keepdims=True)
axs[2].imshow(f_leaves)
axs[2].set_title('Average')
# Luminosity Method
weights = [0.2989, 0.5870, 0.1140]
weighted_mean = np.tensordot(f_leaves, weights, axes=[-1, -1])[..., None]
f_leaves[:] = weighted_mean.astype(f_leaves.dtype)
'''f_leaves[:, :, 0] = np.dot(f_leaves[:, :, 0], 0.2989)
f_leaves[:, :, 1] = np.dot(f_leaves[:, :, 1], 0.5870)
f_leaves[:, :, 2] = np.dot(f_leaves[:, :, 2], 0.1140)
f_leaves[:, :, :] = f_leaves[:, :, 0] + f_leaves[:, :, 1] + f_leaves[:, :, 2]'''
axs[3].imshow(f_leaves)
axs[3].set_title('Luminosity')
plt.show()

# Luminosity accounts for human perception
