import os

extension = ".py"

files = os.listdir()

print(f"Files with '{extension}' extension: \n")

count = 0

for file in files:
    if file.endswith(extension):
        print(file)
        count += 1

print(f"\nTotal {extension} files: {count}")


