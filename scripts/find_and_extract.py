#!/usr/bin/env python3
import zipfile
import os
import glob

# Search for zip file
search_paths = [
    '/vercel/share/v0-project',
    '/home/user',
    os.getcwd(),
    os.path.expanduser('~')
]

zip_file = None
for search_path in search_paths:
    if os.path.exists(search_path):
        pattern = os.path.join(search_path, '*.zip')
        matches = glob.glob(pattern)
        if matches:
            zip_file = matches[0]
            print(f"Found zip file: {zip_file}")
            break

if not zip_file:
    print("Error: No zip file found")
    print(f"Searched in: {search_paths}")
    exit(1)

# Extract to /vercel/share/v0-project
extract_path = '/vercel/share/v0-project'
print(f"Extracting to: {extract_path}")

with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

print("Extraction complete!")

# List some extracted files
for root, dirs, files in os.walk(extract_path):
    # Skip scripts directory
    if 'scripts' in root:
        continue
    for file in files[:5]:
        print(f"  {os.path.join(root, file)[:80]}")
    if len(files) > 5:
        print(f"  ... and {len(files) - 5} more files")
    break
