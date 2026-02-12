#!/usr/bin/env python3
import zipfile
import os
import sys

# The zip file is in the current working directory
cwd = os.getcwd()
zip_file = os.path.join(cwd, 'earnovadigitalhub (3).zip')

print(f"Current working directory: {cwd}")
print(f"Looking for zip file at: {zip_file}")
print(f"Zip file exists: {os.path.exists(zip_file)}")

if os.path.exists(zip_file):
    print("Extracting zip file...")
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(cwd)
    print("Extraction complete!")
    
    # List extracted files
    print("\nExtracted files:")
    for root, dirs, files in os.walk(cwd):
        level = root.replace(cwd, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 2 * (level + 1)
        for file in files[:10]:  # Limit output
            print(f'{subindent}{file}')
        if len(files) > 10:
            print(f'{subindent}... and {len(files) - 10} more files')
        if level > 2:  # Limit depth
            break
else:
    print(f"Error: Zip file not found at {zip_file}")
    sys.exit(1)
