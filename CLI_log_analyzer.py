import argparse

def analyze_logs(file, level):

    count = 0 

    with open(file, "r") as f:

        for line in f: 
            if level in line :
                count += 1
    print(f"{level} count:{count}")

def main():

    parser = agrparse.ArgumentParser()

    parser.add_argument("file", help = "log file name")
    parser.add_argument("level", help = "log level (ERROR, INFO, WARNING)")

    args = parser_args()

    analyze_logs(args.files, args.level)

    main()

        