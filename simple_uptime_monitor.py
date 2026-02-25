import random

services = ["auth-service", "payment-service", "user-service", "API-gateway"]

down_count = 0

print("Service health report")
print("---------------------")

for service in services:
    status = random.choice(["UP", "DOWN"])

    print(f"{service}: {status}")

    if status == "DOWN":
        down_count += 1
print("\nSummary:")
print("--------")
print(f"Total services : {len(services)}")
print(f"\nTotal services down: {down_count}")
