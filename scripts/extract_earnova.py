#!/usr/bin/env python3
import zipfile
import os

zip_file = '/vercel/share/v0-project/earnovadigitalhub (3).zip'
extract_dir = '/vercel/share/v0-project/earnova'

# Create extraction directory
os.makedirs(extract_dir, exist_ok=True)

# Extract the zip file
try:
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"Successfully extracted to {extract_dir}")
    
    # List first few extracted files
    for root, dirs, files in os.walk(extract_dir):
        level = root.replace(extract_dir, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        if level < 2:  # Only show first 2 levels
            subindent = ' ' * 2 * (level + 1)
            for file in files[:5]:
                print(f"{subindent}{file}")
except Exception as e:
    print(f"Error: {e}")
