import argparse
import subprocess

def run_command(command):

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    print("output:\n")
    print(result.stdout)

    if result.stderr:
        print("Error:\n")
        print(result.stderr)

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--command", required=True, help="command to run")

    args = parser.parse_args()

    run_command(args.command)

main()