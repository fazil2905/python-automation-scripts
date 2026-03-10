import psutil

def check_cpu (threshold=80):

    cpu_usage = psutil.cpu_percent (interval=1)

    print(f"cpu_usage : {cpu_usage}%")

    if cpu_usage >= threshold:
        print("High cpu usage detected")

    else:
        print("cpu usage normal")

def main():
    check_cpu()

main()

