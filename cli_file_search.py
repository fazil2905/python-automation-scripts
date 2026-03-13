import os
import sys


def search_keyword(directory, keyword):

    print(f"Searching for '{keyword}'...\n")

    for file in os.listdir(directory):

        path = os.path.join(directory, file)

        if os.path.isfile(path):

            try:
                with open(path, "r", errors="ignore") as f:

                    for line in f:

                        if keyword in line:
                            print(f"{file} -> {line.strip()}")

            except:
                pass


def main():
    if len(sys.argv) < 2:
        print("usage: python cli_file_search.py <keyword>")
        return

    keyword = sys.argv[1]

    search_keyword(".", keyword)


main()
