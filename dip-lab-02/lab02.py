import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
 
IMAGE_PATH = "my_image.png"  # <-- change to your own image's filename
 
# Step 2: Load the image 
bgr = cv.imread(IMAGE_PATH)
if bgr is None:
    raise FileNotFoundError(f"Image not found or unreadable: {IMAGE_PATH}")
 
print("Step 2: Load")
print("Image shape (H, W, C):", bgr.shape)
print("Data type:", bgr.dtype)


# Step 3: Inspect 
h, w, c = bgr.shape
cy, cx = h // 2, w // 2
 
print("\nStep 3: Inspect")
print("Height:", h)
print("Width:", w)
print("Channels:", c)
print("Top-left pixel [0, 0] (BGR):", bgr[0, 0])
print(f"Center pixel [{cy}, {cx}] (BGR):", bgr[cy, cx])
print("Global min:", bgr.min(), "| Global max:", bgr.max())
for i, name in enumerate(["Blue", "Green", "Red"]):  # OpenCV order is BGR
    print(f"{name} channel -> min: {bgr[:, :, i].min()}, max: {bgr[:, :, i].max()}")

 # Step 4: Colors and channels 
rgb = cv.cvtColor(bgr, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(bgr, cv.COLOR_BGR2GRAY)
red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
 
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
panels = [
    (rgb, "RGB (correct display)", None),
    (red, "Red channel", "gray"),
    (green, "Green channel", "gray"),
    (blue, "Blue channel", "gray"),
    (gray, "Grayscale", "gray"),
    (bgr, "Unconverted BGR (wrong colors)", None),
]
for ax, (img, title, cmap) in zip(axes.ravel(), panels):
    ax.imshow(img, cmap=cmap)
    ax.set_title(title)
    ax.axis("off")
plt.tight_layout()
plt.savefig("channels_figure.png", dpi=120)
 
r, g, b = (int(v) for v in rgb[cy, cx])
hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
print("\nStep 4: Colors")
print(f"Center pixel RGB: ({r}, {g}, {b})")
print("Center pixel HEX:", hex_color)

#  Step 5: Crop, resize, save
y_start, x_start = max(cy - 50, 0), max(cx - 50, 0)
y_end, x_end = y_start + 100, x_start + 100
crop = rgb[y_start:y_end, x_start:x_end]
print("\nStep 5: Crop / Resize")
print("Crop shape:", crop.shape)
 
resized = cv.resize(crop, (200, 200))  # (width, height)
print("Resized shape:", resized.shape)
 
fig, axes = plt.subplots(1, 3, figsize=(14, 5))
for ax, img, title in zip(
    axes,
    [rgb, crop, resized],
    ["Original", "Crop (100x100)", "Resized (200x200)"],
):
    ax.imshow(img)
    ax.set_title(title)
    ax.axis("off")
plt.tight_layout()
plt.savefig("crop_resize_figure.png", dpi=120)
 
resized_bgr = cv.cvtColor(resized, cv.COLOR_RGB2BGR)
ok = cv.imwrite("resized_crop.png", resized_bgr)
print("cv.imwrite saved resized_crop.png successfully:", ok)

#  Step 6: Histogram 
plt.figure(figsize=(8, 5))
plt.hist(gray.flatten(), bins=256, range=(0, 256), color="gray")
plt.title("Grayscale Histogram")
plt.xlabel("Pixel intensity (0-255)")
plt.ylabel("Number of pixels")
plt.tight_layout()
plt.savefig("grayscale_histogram.png", dpi=120)
print("\nStep 6: Histogram")
print("Mean gray intensity:", round(float(gray.mean()), 2))


# Step 7: Bit depth 
gradient = np.tile(np.arange(256, dtype=np.uint8), (100, 1))
 
 
def quantize(img, bits):
    levels = 2 ** bits
    step = 256 // levels
    scale = 255 // (levels - 1)
    return ((img // step) * scale).astype(np.uint8)
 
 
grads = [
    (gradient, "8-bit (256 levels)"),
    (quantize(gradient, 1), "1-bit (2 levels)"),
    (quantize(gradient, 2), "2-bit (4 levels)"),
    (quantize(gradient, 4), "4-bit (16 levels)"),
]
 
fig, axes = plt.subplots(4, 1, figsize=(8, 6))
for ax, (img, title) in zip(axes, grads):
    ax.imshow(img, cmap="gray", vmin=0, vmax=255)
    ax.set_title(title)
    ax.axis("off")
plt.tight_layout()
plt.savefig("bit_depth_figure.png", dpi=120)
 
print("\nStep 7: Bit depth ")
for img, title in grads:
    print(f"{title}: unique values = {len(np.unique(img))}")
 
plt.show()