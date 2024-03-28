import requests
import csv

# Settings
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
csvfilepath = "heime_token.csv"
access_token = ""

# Find token in CSV File
with open(csvfilepath, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    value_index = header.index('value')
    for row in csvreader:
        if row[0] == 'access_token':
            access_token = row[value_index]

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
