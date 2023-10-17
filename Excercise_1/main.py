import numpy as np
import matplotlib.pyplot as plt

lena_file_path = "lenabin.sec"
peppers_file_path = "peppersbin.sec"

image_width = 256
image_height = 256

with open(lena_file_path, 'rb') as f:
    lena_data = np.fromfile(f, dtype=np.uint8, count=image_width * image_height)
    lena_image = lena_data.reshape(image_height, image_width)

with open(peppers_file_path, 'rb') as f:
    peppers_data = np.fromfile(f, dtype=np.uint8, count=image_width * image_height)
    peppers_image = peppers_data.reshape(image_height, image_width)

plt.figure(figsize=(12, 4))
plt.subplot(141)
plt.title('Lena Image')
plt.imshow(lena_image, cmap='gray')
plt.axis('off')

plt.subplot(142)
plt.title('Peppers Image')
plt.imshow(peppers_image, cmap='gray')
plt.axis('off')

lena_left_half = lena_image[:, :image_width // 2]
peppers_right_half = peppers_image[:, image_width // 2:]

J = np.zeros((image_height, image_width), dtype=np.uint8)
J[:, :image_width // 2] = lena_left_half
J[:, image_width // 2:] = peppers_right_half

plt.subplot(143)
plt.title('J Image')
plt.imshow(J, cmap='gray')
plt.axis('off')

K = np.zeros_like(J)
K[:, :image_width // 2] = J[:, image_width // 2:]
K[:, image_width // 2:] = J[:, :image_width // 2]

plt.subplot(144)
plt.title('K Image')
plt.imshow(K, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
