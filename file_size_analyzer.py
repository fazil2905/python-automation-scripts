import os 

files = os.listdir()

total_size = 0

for file in files:
    if os.path.isfile(file):
        size = os.path.getsize(file)
        print(f"{file} - {size} bytes")
        total_size += size
        
print(f"\nTotal size of all files: {total_size} bytes")

