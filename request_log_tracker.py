file_name = "sample.log"

total_requests = 0
total_error = 0
ip_count = {}
unique_ips = set()

with open(file_name, "r") as file:
    for line in file:
        total_requests += 1

        if "ERROR" in line:
            total_error += 1

        words = line.strip().split()
        for word in words:
            if "." in word:
                unique_ips.add(word)

                if word in ip_count:
                    ip_count[word] += 1
                else:
                    ip_count[word] = 1

most_frequent_ip = max(ip_count, key=ip_count.get)

print("Request log summary:")
print("-------------------")
print(f"Total requests: {total_requests}")
print(f"Total ERROR requests: {total_error}")
print(f"Unique IP addresses: {len(unique_ips)}")
print(f"Most frequent IP address: {most_frequent_ip}")