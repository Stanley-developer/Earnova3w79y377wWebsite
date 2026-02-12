import os
import sys

path = '/vercel/share/v0-project'
print(f"Contents of {path}:")
print(os.listdir(path))
print()

# Find zip files
for item in os.listdir(path):
    if 'zip' in item.lower():
        full_path = os.path.join(path, item)
        print(f"Found: {item}")
        print(f"Full path: {full_path}")
        print(f"Exists: {os.path.exists(full_path)}")
        print(f"Is file: {os.path.isfile(full_path)}")
