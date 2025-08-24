# Append text at the end of an image (for watermark or hidden data)
with open("copy.jpg", "ab") as f:
    f.write(b"\n# Hidden message at end of file")
print("Data appended to image.")
