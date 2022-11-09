#!/usr/bin/python3
from functools import cmp_to_key
import os

ROOT = "release-notes"


def print_red(text): print("\033[91m{}\033[00m".format(text))
def print_green(text): print("\033[92m{}\033[00m".format(text))


# Get a list of all folders in the release-notes directory
# For each folder, append the folder name to the index.txt file
folders = [x for x in os.listdir(ROOT) if os.path.isdir(f"{ROOT}/{x}")]

# Make sure the folders are all valid versions
for folder in folders:
    if not folder.replace(".", "").isnumeric() or folder.count(".") != 2:
        print_red(
            f"Invalid folder name: \"{folder}\". Must be in the format x.y.z")
        exit(1)

print(f"Found {len(folders)} folders")

sorted_folders = folders.sort(key=lambda x: [int(y) for y in x.split('.')])


with open(f"{ROOT}/index.txt", "w") as index:
    for folder in folders:
        if not os.path.isfile(folder):
            index.write(folder + "\n")

print_green("Index file updated successfully!")
