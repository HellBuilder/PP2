# rite a Python program to copy the contents of a file to another file.
def copy_file(source, destination):
    with open(source, "r", encoding="utf-8") as src, open(destination, "w", encoding="utf-8") as dest:
        dest.write(src.read())

copy_file(r"C:\Users\Aphelios\Documenets\GitHub\PP2\Lab6\files_and_dirs\source.txt", r"C:\Users\Aphelios\Documenets\GitHub\PP2\Lab6\files_and_dirs\destinationt.txt")
