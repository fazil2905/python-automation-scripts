file_name = "sample.log"

count = 0

with open(file_name, "r") as file:
    for line in file:
        print(line.strip())
        count += 1

print(f"\nTotal lines: {count}")
