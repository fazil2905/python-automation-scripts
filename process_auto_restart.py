import psutil
import os

def monitor_process(process_name):

    running = False

    for proc in psutil.process_iter(["name"]):

        if "python" in proc.info["name"]:
            running = True
            break

    if running:
        print(f"{process_name} is Running")

    else:
        print(f"{process_name} Stopped. Restarting...")
        os.system (process_name)

def main():
    monitor_process("python")

main()
