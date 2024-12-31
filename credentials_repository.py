import json

CREDENTIALS_FILE = "resources/credentials.json"

def add_credentials(website, email, password):
    new_creds = {
        website.lower(): {
            "email": email,
            "password": password
        }
    }

    try:
        with open(CREDENTIALS_FILE, "r") as credentials_file:
            existing_credentials_data = json.load(credentials_file)
            print(existing_credentials_data)
    except FileNotFoundError:
        with open(CREDENTIALS_FILE, "w") as credentials_file:
            json.dump(new_creds, credentials_file, indent=4)
    else:
        with open(CREDENTIALS_FILE, "w") as credentials_file:
            existing_credentials_data.update(new_creds)
            json.dump(existing_credentials_data, credentials_file, indent=4)


def search_website(website):
    try:
        with open(CREDENTIALS_FILE, "r") as credentials_file:
            existing_credentials_data = json.load(credentials_file)
            print(type(existing_credentials_data))
            print(existing_credentials_data)

    except FileNotFoundError:
        return None

    else:
        for key, value in existing_credentials_data.items():
            print(key)
            if key == website.lower():
                return value["email"], value["password"]
        return None