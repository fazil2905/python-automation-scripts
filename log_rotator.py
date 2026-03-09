import os 

def rotate_log(file_name, max_size_mb = 1):

    if not os.path.exists(file_name):
        print("log file does not exist")
        return
    
    size = os.path.getsize(file_name)

    max_size = max_size_mb * 1024 * 1024

    if size >= max_size:

        archived = file_name + ".1"

        os.rename(file_name, archived)

        open(file_name, "W").close()

        print(f"Log Rotated : {archived}")

    else:
        print ("Log size within limit")

def main():

    rotate_log("app.log")

main()
