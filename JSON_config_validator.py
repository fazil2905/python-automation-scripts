import json

def load_config(file_name):
    with open(file_name, "r") as file:
        return json.load(file)

def validate_config(config, required_keys):
    missing_keys = []

    for key in required_keys:
        if key not in config:
            missing_keys.append(key)

    return missing_keys

def main():
    file_name = "config.json"
    required_keys = ["app_name", "version", "port", "debug"]
    
    config = load_config(file_name)
    missing = validate_config(config, required_keys)

    if missing:
        print("Missing keys:", missing)
    else:
        print("All required keys are present.")

main()