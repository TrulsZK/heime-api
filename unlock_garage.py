import requests
import json

# Settings
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
jsonfilepath = "heime_token.json"
access_token = ""

# Find token in JSON File
with open(jsonfilepath, "r") as jsonfile:
    token_data = json.load(jsonfile)
    access_token = token_data.get("access_token")

# Start Session
session = requests.Session()

start_url = "https://app.heime.com/"
start_payload = {}

start_response = session.post(start_url, json=start_payload, headers=headers)

# Unlock
unlock_url = "https://app.heime.com/en/api/v1/cooperatives/0/locks/0/unlock"
unlock_headers = {
    "accept": "application/json",
    "authorization": "Bearer " + access_token,
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
unlock_payload = {}

unlock_response = session.post(unlock_url, json=unlock_payload, headers=unlock_headers)

print(unlock_response.json())
