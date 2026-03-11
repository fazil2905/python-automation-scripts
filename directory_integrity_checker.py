import os

def check_directory(directory, previous_files):

    current_files = set(os.listdir(directory))

    new_files = current_files - previous_files
    deleted_files = previous_files - current_files

    if new_files:
        print(f"New files detected : {new_files}")

    if deleted_files:
        print(f"Files removed : {deleted_files}")

    if not new_files and not deleted_files:
        print("No changes detected")

def main():
    
    directory = "."

    previous_files = set(os.listdir(directory))

    input = ("press ENTER to check directory again")

    check_directory(directory, previous_files)

main()