def detect_failed_logins(file_name, threshold=3):

    ip_attempts = {}

    with open(file_name, 'r') as file:
        for line in file:
            
            words = line.split()

            if "from" in words :
                ip = words[words.index("from") + 1]

                if ip in ip_attempts:
                    ip_attempts[ip] += 1
                else:
                    ip_attempts[ip] = 1

    print("Suspicious IP detected:")

    for ip, count in ip_attempts.items():
        if count >= threshold:
            print(f"IP: {ip}, Failed Attempts: {count}")

def main():
    detect_failed_logins('auth.log')

main() 