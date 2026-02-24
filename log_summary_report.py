file_name = "sample.log"

total = 0
error_count = 0
warning_count = 0
info_count = 0

with open(file_name, "r") as file:
    for line in file:
        total += 1
        if "ERROR" in line:
            error_count += 1
        elif "WARNING" in line:
            warning_count += 1
        elif "INFO" in line:
            info_count += 1

print("LOG SUMMARY REPORT")
print("----------------------")
print(f"Total lines in log: {total}")
print(f"ERROR count: {error_count}")
print(f"WARNING count: {warning_count}")
print(f"INFO count: {info_count}")
