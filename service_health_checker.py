import requests

def check_services(services):
    
    print("checking services...\n")

    for service in services :

        try:
            response = requests.get(service, timeout = 5)

            if response.status_code == 200:
                print(f"{service} -> OK ({response.status_code})")

            else:
                print(F"{service} -> DOWN ({response.status_code})")

        except requests.exceptions.RequestException:
            print (f"{service} -> DOWN")

def main():

    services = [
        "https://api.github.com",
        "https://google.com"
    ]
    check_services(services)

main()