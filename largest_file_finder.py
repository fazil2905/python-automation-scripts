import os 

def get_largest_files(directory):
    files_data = []

    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)

        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            files_data.append((item, size))

    files_data.sort(key=lambda x: x[1], reverse=True)

    return files_data

def print_largest_files(files_data, top_n=5):
    print("Top Largest Files:")
    print("-------------------")

    for file, size in files_data[:top_n]:
        print(f"{file}: {size} bytes")

def main():
    directory = "."
    files = get_largest_files(directory)
    print_largest_files(files)

main()

