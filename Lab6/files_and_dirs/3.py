# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.
import os

def check_path(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("Path does not exist.")

path = r"C:\Users\Aphelios\Documenets\GitHub\PP2\Lab6\files_and_dirs\test.txt"
check_path(path)