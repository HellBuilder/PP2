# Write a Python program to write a list to a file.
def write_list_to_file(filename, my_list):
    with open(filename, "w", encoding="utf-8") as file:
        for item in my_list:
            file.write(f"{item}\n")

items = ["Apple", "Banana", "Cherry"]
write_list_to_file("fruits.txt", items)
