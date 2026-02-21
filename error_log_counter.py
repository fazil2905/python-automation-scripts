file_name = "sample.log"

error_count = 0

with open(file_name, "r") as file:
    for line in file:
        if "ERROR" in line:
            error_count += 1

print(f"Total ERROR lines: {error_count}")

