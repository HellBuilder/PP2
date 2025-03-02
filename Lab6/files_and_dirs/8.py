# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.
import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' deleted successfully.")
        else:
            print("Permission denied. Cannot delete.")
    else:
        print("File does not exist.")

delete_file(r"C:\Users\Admin\Desktop\PP2-Repos\PP2\TSIS6_LAB6\files_and_dirs\test.txt")
