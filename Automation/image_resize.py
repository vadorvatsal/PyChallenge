from PIL import Image
import os

print(f"Current working directory: {os.getcwd()}")

images = [file for file in os.listdir("/Users/vatsalvador/Desktop/sourceLogos/") if file.endswith('png')]
total_images = len(images)

for image in images:
    try:
        img = Image.open("/Users/vatsalvador/Desktop/sourceLogos/" + image)
        img.save("/Users/vatsalvador/Desktop/resize/" + image, optimize=True, quality=30)
    except:
        print("Error !")

print("Completed")
