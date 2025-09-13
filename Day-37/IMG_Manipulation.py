"""
📌 Practical Practice - IMG manipulation
"""
from PIL import Image
import numpy as np

# IMG Manipulation

# Load image
img = Image.open("image.jpg")  # PIL Image object
img_array = np.array(img)        # Convert to NumPy array
print("Shape:", img_array.shape)  # (height, width, number of color channels (R, G, B)) -> Shape: (1328, 2048, 3)

# Convert to grayscale
# 👉🏻 axis=2 means last dimension , which is colour
# .mean() , take average of R, G, B for each pixel.
# 👉🏻 NumPy averages produce float numbers by default (like 150.333...).
# Images usually require integer values 0–255.
# astype(np.uint8) converts the floats to 8-bit unsigned integers.

choice = input("1. Grey\n2. Red\n3. Green\n4. Blue\n5. Custom")
if choice.strip() == "1":
    gray = img_array.mean(axis=2).astype(np.uint8)
    gray_img = Image.fromarray(gray)
    gray_img.save("Output.jpg")
elif choice.strip() == "2":
    red_only = img_array.copy()
    red_only[:, :, 1] = 0  # zero out green
    red_only[:, :, 2] = 0  # zero out blue
    red = Image.fromarray(red_only)
    red.save("Output.jpg")
elif choice.strip() == "3":
    green_only = img_array.copy()
    green_only[:, :, 0] = 0  # zero out red
    green_only[:, :, 2] = 0  # zero out blue
    green = Image.fromarray(green_only)
    green.save("Output.jpg")
elif choice.strip() == "4":
    blue_only = img_array.copy()
    blue_only[:, :, 0] = 0  # zero out red
    blue_only[:, :, 1] = 0  # zero out green
    blue = Image.fromarray(blue_only)
    blue.save("Output.jpg")
elif choice.strip() == "5":
    red_mult = float(input("Multiplier for Red (e.g., 1.0): "))
    green_mult = float(input("Multiplier for Green (e.g., 1.0): "))
    blue_mult = float(input("Multiplier for Blue (e.g., 1.0): "))

    # Convert to float to avoid overflow
    custom_img_array = img_array.astype(np.float32)

    # Apply multipliers
    custom_img_array[:, :, 0] *= red_mult  # Red channel
    custom_img_array[:, :, 1] *= green_mult  # Green channel
    custom_img_array[:, :, 2] *= blue_mult  # Blue channel

    # Clip values and convert back to uint8
    custom_img_array = np.clip(custom_img_array, 0, 255).astype(np.uint8)

    # Save
    custom = Image.fromarray(custom_img_array)
    custom.save("Output.jpg")
elif choice.strip() == "6":
    print("Enter crop coordinates (x1, y1) to (x2, y2):")
    x1 = int(input("x1 (left): "))
    y1 = int(input("y1 (top): "))
    x2 = int(input("x2 (right): "))
    y2 = int(input("y2 (bottom): "))

    height, width = img_array.shape[:2]
    x1, x2 = max(0, x1), min(width, x2)
    y1, y2 = max(0, y1), min(height, y2)

    cropped_array = img_array[y1:y2, x1:x2]
    cropped_image = Image.fromarray(cropped_array)
    cropped_image.save("Output.jpg")
    print(f"Cropped image saved as Cropped_Output.jpg ({x2-x1}x{y2-y1})")

elif choice.strip() == "7":
    bright_val = int(input("Increase brightness by: "))
    bright = np.clip(img_array + bright_val, 0, 255).astype(np.uint8)
    bright_img = Image.fromarray(bright)
    bright_img.save("Output.jpg")
else:
    raise ValueError("Invalid choice")

