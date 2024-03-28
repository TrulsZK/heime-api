# Reverse engineer of Heime API / Heime App

Unofficial Python scripts allowing you to interact with the Heime API. e.g. To automate interactions with the API/App or integrate with other services e.g. Home Assistant using shell_command.

The Heime app https://www.heime.com/en is used as communication platform for neighbourhoods, it also allows you to e.g. unlock doors.

## Script Files

- `get_token.py` - Get `access_token` and `refresh_token` from the API using SMS code
- `refresh_token.py` - Use refresh_token to get a new `access_token`
- `unlock_garage.py` - Example script to interact with the API (in this case unlock the garage in the apartment complex)
- `heime_token.csv` - CSV file to store the `access_token` and `refresh_token`

## Config

1. Go to https://app.heime.com/ and use the Develoepr Tools to get the `client_secret`
2. Open `get_token.py` and `refresh_token.py` and add the `client_secret` and your mobile phone number `loginmobilenumber`
3. Run `get_token.py` and input the code you will receive via SMS
4. `heime_token.csv` has been updated with your tokens and is ready for use

## Usage

- Run `refresh_token.py` to refresh the `access_token`
- Run `unlock_garage.py` to unlock garage (this is just an example file and you will have to add your own API endpoint for it to work)
