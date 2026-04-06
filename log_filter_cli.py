import argparse

def filter_logs(file_name, keyword, output_file=None):

    matched_lines = []

    with open(file_name, "r") as file:
        for line in file:
            if keyword in line:
                matched_lines.append(line.strip())

    print(f"\nMatching lines for '{keyword}':\n")

    for line in matched_lines:
        print(line)

    if output_file:
        with open(output_file, "w") as out:
            for line in matched_lines:
                out.write(line + "\n")

        print(f"\nSaved output to {output_file}")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--file", required=True, help="log file path")
    parser.add_argument("--keyword", required=True, help="keyword to search")
    parser.add_argument("--output", help="optional output file")

    args = parser.parse_args()

    filter_logs(args.file, args.keyword, args.output)


main()