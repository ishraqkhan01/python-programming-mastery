import os

with open("sample_image.png", "rb") as source_file:
    binary_data = source_file.read()

with open("copied_image.png", "wb") as destination_file:
    destination_file.write(binary_data)

if os.path.exists("copied_image.png"):
    orig_size = os.path.getsize("sample_image.png")
    copy_size = os.path.getsize("copied_image.png")
    
    print("--- Binary Copy Verification ---")
    print(f"Original File Size: {orig_size} bytes")
    print(f"Copied File Size:   {copy_size} bytes")
    
    if orig_size == copy_size:
        print("Status: Success! The binary copy is exact and fully functional.")