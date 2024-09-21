import requests
import json

# Settings
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
loginmobilenumber = "+4700000000"
loginpin = 0000
jsonfilepath = "heime_token.json"
client_secret = "xxxxxxxxxxxx"

# Start Session
session = requests.Session()

start_url = "https://app.heime.com/"
start_payload = {}

start_response = session.get(start_url, json=start_payload, headers=headers)

xsrf_token = session.cookies.get("XSRF-TOKEN")

# Enter Mobile phone number
loginmobilenumber_url = "https://app.heime.com/en/api/v1/check"
loginmobilenumber_headers = {
    "accept": "application/json",
    "X-XSRF-TOKEN": str(xsrf_token),
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}
loginmobilenumber_payload = {"phone": loginmobilenumber}

loginmobilenumber_response = session.post(loginmobilenumber_url, json=loginmobilenumber_payload, headers=loginmobilenumber_headers)

print(loginmobilenumber_response.json())

# Ask for SMS Code
loginpin = input("Enter Code From SMS: ")

# Login with PIN
loginpin_url = "https://app.heime.com/en/api/v1/oauth/token"
loginpin_payload = {"username": str(loginmobilenumber), "password": str(loginpin), "grant_type": "password", "client_id": 1, "client_secret": client_secret}

loginpin_response = session.post(loginpin_url, json=loginpin_payload, headers=headers)

print(loginpin_response.json())

# Write to JSON
with open(jsonfilepath, "w") as jsonfile:
    json.dump(loginpin_response.json(), jsonfile, indent=4)
    print("JSON Updated")
