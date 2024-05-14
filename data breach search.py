import requests
from bs4 import BeautifulSoup
import re

def scan_breaches(username, password):
    # Search known data breach databases
    url = "https://haveibeenpwned.com/api/v3/breachedaccount/{}".format(username)
    headers = {"hibp-api-key": "YOUR_API_KEY_HERE"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        breaches = response.json()
        for breach in breaches:
            if password in breach["PwnedPasswords"]:
                return True
    
    return False

# Example usage
if scan_breaches("example_username", "example_password"):
    print("Credentials found in data breaches!")
else:
    print("Credentials not found in data breaches.")
