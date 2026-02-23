import shutil

print("===DISK CHECKER===")

total, used, free = shutil.disk_usage("/")

gb = 1024 ** 3

total_gb = total / gb
used_gb = used / gb
free_gb = free / gb

print(f"Total disk space: {total_gb:.2f} GB")
print(f"Used disk space: {used_gb:.2f} GB")
print(f"Free disk space: {free_gb:.2f} GB")
