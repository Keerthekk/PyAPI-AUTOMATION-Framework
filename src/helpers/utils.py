
import json

def get_payload_auth():
    # Read from the auth json & return json
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data

def common_headers():
    headers = {
        "content-Type": "application/json",
    }
    return headers
