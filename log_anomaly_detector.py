def detect_log_anomaly(file_name, threshold=5):
    
    error_count = 5

    with open(file_name, "r") as file:

        for line in file:

            if "ERROR" in line:
                error_count += 1

    print(f"Total errors found : {error_count}")

    if error_count >= threshold:
        print("LOG ANOMALY DETECTED")

    else:
        print("Log status normal")

def main():
    detect_log_anomaly("sample.log")

main()