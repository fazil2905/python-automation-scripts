import shutil

def check_disk_usage(path = "/" , threshold = 80):

    total, used, free = shutil.disk_usage(path)

    usage_percent = (used / total) * 100

    print(f"Disk usage: {usage_percent:.2f}%")

    if usage_percent > threshold:
        print("Status: WARNING - Disk usage above threshold")
    else:
        print("Status: OK")

def main():
    check_disk_usage()

main()