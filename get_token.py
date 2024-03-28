import requests
import csv

# Settings
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
loginmobilenumber = 00000000
loginpin = 0000
csvfilepath = "heime_token.csv"
client_secret = "XXXXXX"

# Start Session
session = requests.Session()

start_url = "https://app.heime.com/"
start_payload = {}

start_response = session.post(start_url, json=start_payload, headers=headers)

# Enter Mobile phone number
loginmobilenumber_url = "https://app.heime.com/en/api/v1/check"
loginmobilenumber_payload = {"phone": str(loginmobilenumber)}

loginmobilenumber_response = session.post(loginmobilenumber_url, json=loginmobilenumber_payload, headers=headers)

print(loginmobilenumber_response.json())

# Ask for SMS Code
loginpin = input("Enter Code From SMS: ")

# Login with PIN
loginpin_url = "https://app.heime.com/en/api/v1/oauth/token"
loginpin_payload = {"username": str(loginmobilenumber), "password": str(loginpin), "grant_type": "password", "client_id": 1, "client_secret": client_secret}

loginpin_response = session.post(loginpin_url, json=loginpin_payload, headers=headers)

print(loginpin_response.json())

# Set tokens as var
login_token_type = loginpin_response.json()["token_type"]
login_expires_in = loginpin_response.json()["expires_in"]
login_access_token = loginpin_response.json()["access_token"]
login_refresh_token = loginpin_response.json()["refresh_token"]

# Write to CSV
with open(csvfilepath, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["key", "value"])
    csvwriter.writerow(["token_type", login_token_type])
    csvwriter.writerow(["expires_in", login_expires_in])
    csvwriter.writerow(["access_token", login_access_token])
    csvwriter.writerow(["refresh_token", login_refresh_token])
    print("CSV Updated")

