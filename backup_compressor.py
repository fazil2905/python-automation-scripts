import os
import zipfile

def create_backup(directory, backup_name):

    with zipfile.ZipFile(backup_name, "w") as backup:

        for file in os.listdir(directory):

            path = os.path.join(directory, file)

            if os.path.isfile (path):

                backup.write(path)

    print(f"Backup created : {backup_name}")

def main():

    create_backup(".", "backup.zip")

main()