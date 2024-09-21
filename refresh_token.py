import requests
import json

# Settings
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
jsonfilepath = "heime_token.json"
refresh_token = ""
client_secret = "xxxxxxxxxxxx"

# Find token in JSON File
with open(jsonfilepath, "r") as jsonfile:
    token_data = json.load(jsonfile)
    refresh_token = token_data.get("refresh_token")

# Start Session
session = requests.Session()

start_url = "https://app.heime.com/"
start_payload = {}

start_response = session.post(start_url, json=start_payload, headers=headers)

# Login with refresh_token
loginrefresh_url = "https://app.heime.com/en/api/v1/oauth/token"
loginrefresh_payload = {"refresh_token": refresh_token, "grant_type": "refresh_token", "client_id": 1, "client_secret": client_secret}

loginrefresh_response = session.post(loginrefresh_url, json=loginrefresh_payload, headers=headers)

print(loginrefresh_response.json())

# Set tokens as var
login_token_type = loginrefresh_response.json()["token_type"]
login_expires_in = loginrefresh_response.json()["expires_in"]
login_access_token = loginrefresh_response.json()["access_token"]
login_refresh_token = loginrefresh_response.json()["refresh_token"]

# Write to JSON
with open(jsonfilepath, "w") as jsonfile:
    json.dump(loginrefresh_response.json(), jsonfile, indent=4)
    print("JSON Updated")
