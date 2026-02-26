file_name = "activity.log"

log_count = 0
error_count = 0
unique_users = set()
user_count = {}

with open(file_name, "r") as file:
    for line in file:
        log_count += 1
        

        if "ERROR" in line:
            error_count += 1

        words = line.strip().split()

        for word in words:
            if word.startswith("user="):

                user = word.split("=")[1]

                unique_users.add(user)
                    

                if user in user_count:
                    user_count[user] += 1
                else:
                    user_count[user] = 1

most_active_user = max(user_count, key=user_count.get) 

print(f"Total log entries: {log_count}")
print(f"Total ERROR entries: {error_count}")
print(f"Total unique users: {len(unique_users)}")
print(f"Most active user: {most_active_user}")