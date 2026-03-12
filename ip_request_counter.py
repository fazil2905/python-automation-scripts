def count_ip_requests(file_name):

    ip_count = {}

    with open(file_name, "r") as file:

        for line in file:

            parts = line.split()

            if len(parts) > 0:
                ip = parts[0]

                if ip in ip_count:
                    ip_count[ip] += 1
                else:
                    ip_count[ip] = 1

    print ("Request count per ip:")

    for ip, count in ip_count.items():
        print(f"{ip}: {count}")

def main():
    count_ip_requests("sample.log")

main()