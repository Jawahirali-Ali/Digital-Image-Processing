# Exercise 1: Variables and Data Types
width = 640
height = 480
image_name = "sample.png"
is_color = True
print(width, type(width))
print(height, type(height))
print(image_name, type(image_name))
print(is_color, type(is_color))
print("Total pixels:", width * height)   # 307200

# Exercise 2: if, elif, else
for intensity in [-1, 0, 127, 128, 255, 256]:
    if intensity < 0 or intensity > 255:
        label = "Invalid"
    elif intensity >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"
    print(intensity, "->", label)

# Exercise 3: for and while loops
for value in [20, 130, 255]:
    if value >= 128:
        print(value, "Bright pixel")
    else:
        print(value, "Dark pixel")

counter = 0
while counter < 3:
    print(counter)
    counter += 1        # counter update karna zaroori hai

# Exercise 4: Functions
def is_bright(pixel, threshold=128):
    return pixel >= threshold

print(is_bright(127))        # False
print(is_bright(128))        # True
print(is_bright(200, 210))   # False

# Exercise 5: Lists and Tuples
pixels = [0, 128, 255]
print(pixels[0])
pixels[1] = 150
pixels.append(64)
print(pixels, len(pixels))   # [0, 150, 255, 64] 4

size = (640, 480)
width, height = size
print(width, height)
# A list is mutable, so its items can be changed after creation.
# A tuple is immutable, so its items cannot be changed once created.

# Exercise 6: Dictionaries and Sets
image = {"width": 640, "height": 480}
image["mode"] = "RGB"
print(image["width"], image["mode"])

labels = set(["cat", "dog", "cat", "bird"])
print(len(labels))   # 3