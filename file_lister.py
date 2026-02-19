import os

print("Files in current directory: \n")

files = os.listdir()

count = 0

for file in files:
    print(file)
    count += 1

print("\nTotal files:", count)
