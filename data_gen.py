import numpy as np
import cv2
import matplotlib.pyplot as plt
import random

def generate_random_shape_image(size=28):
    img = np.zeros((size, size), dtype=np.uint8)
    shape = random.choice(['circle', 'square', 'triangle'])
    
    # Create a blank canvas for the shape (larger to avoid crop after rotation)
    shape_canvas = np.zeros((size, size), dtype=np.uint8)
    
    center = (random.randint(8, 20), random.randint(8, 20))
    scale = random.randint(6, 10)  # size of shape

    if shape == 'circle':
        cv2.circle(shape_canvas, center, scale, 255, -1)

    elif shape == 'square':
        top_left = (center[0] - scale, center[1] - scale)
        bottom_right = (center[0] + scale, center[1] + scale)
        cv2.rectangle(shape_canvas, top_left, bottom_right, 255, -1)

    elif shape == 'triangle':
        pt1 = (center[0], center[1] - scale)
        pt2 = (center[0] - scale, center[1] + scale)
        pt3 = (center[0] + scale, center[1] + scale)
        triangle = np.array([pt1, pt2, pt3], np.int32)
        cv2.fillPoly(shape_canvas, [triangle], 255)

    # Apply random rotation
    angle = random.randint(0, 359)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(shape_canvas, M, (size, size), flags=cv2.INTER_NEAREST)

    return rotated, shape

# === Show 10 random images ===
fig, axes = plt.subplots(1, 10, figsize=(15, 2))

for i in range(10):
    img, label = generate_random_shape_image()
    axes[i].imshow(img, cmap='gray')
    axes[i].set_title(label)
    axes[i].axis('off')

plt.tight_layout()
plt.show()
