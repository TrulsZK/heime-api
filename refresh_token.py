import requests
import csv

# Settings
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
csvfilepath = "heime_token.csv"
refresh_token = ""
client_secret = "XXXXXX"

# Find token in CSV File
with open(csvfilepath, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    value_index = header.index('value')
    for row in csvreader:
        if row[0] == 'refresh_token':
            refresh_token = row[value_index]

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

# Write to CSV
with open(csvfilepath, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["key", "value"])
    csvwriter.writerow(["token_type", login_token_type])
    csvwriter.writerow(["expires_in", login_expires_in])
    csvwriter.writerow(["access_token", login_access_token])
    csvwriter.writerow(["refresh_token", login_refresh_token])
    print("CSV Updated")

