def create_and_write_file(album):
    with open('album', 'w') as file:
        file.write("Take a break.\n")
        file.write("Take a picture.\n")
        file.write("Save it for future.\n")

create_and_write_file('sample.txt')
print("File created and written successfully.")
