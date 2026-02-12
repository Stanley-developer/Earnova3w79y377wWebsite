#!/usr/bin/env python3
import zipfile
import os

zip_path = '/vercel/share/v0-project/earnovadigitalhub (3).zip'
extract_path = '/vercel/share/v0-project'

# Extract the zip file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Extraction complete!")
print("Listing extracted files...")
for root, dirs, files in os.walk(extract_path):
    for file in files:
        print(os.path.join(root, file)[:100])
