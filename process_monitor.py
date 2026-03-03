import subprocess
import os

def get_process_list():
    if os.name == 'nt':  # Windows
        command = 'tasklist'
    else:  # Unix/Linux/Mac
        command = 'ps -aux'

    result = subprocess.run(command, capture_output = True, text = True, shell = True)
    return result.stdout

def main():
    processes = get_process_list()
    print("Running Processes:")
    print(processes)

main()