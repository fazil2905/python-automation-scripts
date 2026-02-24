file_name = "sample.log"

unique_ips = set()

with open(file_name, "r") as file:
    for line in file:
        words = line.strip().split()

        for word in words:
            if "." in word:
                unique_ips.add(word)


print("Unique IP Addresses:")
for ip in unique_ips:
    print(ip)

print(f"Total unique IP addresses: {len(unique_ips)}")               