# Copy an image file in binary mode
with open('download.jpg', 'rb') as file:
    binary_data = file.read()

with open('copy.jpg', 'wb') as copy_file:
    copy_file.write(binary_data)

print("Image copied successfully.")
