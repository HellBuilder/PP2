# rite a Python program to copy the contents of a file to another file.
def copy_file(source, destination):
    with open(source, "r", encoding="utf-8") as src, open(destination, "w", encoding="utf-8") as dest:
        dest.write(src.read())

copy_file(r"C:\Users\Admin\Desktop\PP2-Repos\PP2\TSIS6_LAB6\files_and_dirs\source.txt", r"C:\Users\Admin\Desktop\PP2-Repos\PP2\TSIS6_LAB6\files_and_dirs\destinationt.txt")
