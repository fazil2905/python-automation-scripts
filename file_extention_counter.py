import os

def count_file_extentions(directory):

    ext_count = {}

    files = os.listdir(directory)

    for file in files:

        if "." in file:
             ext = file.split(".")[-1]
        
             if ext in ext_count:
                ext_count[ext] += 1
             else:
                ext_count[ext] = 1

    print("File extention summary:\n")

    for ext, count in ext_count.items():
        print(f"{ext}: {count}")

def main():
    
    count_file_extentions(".")

main()