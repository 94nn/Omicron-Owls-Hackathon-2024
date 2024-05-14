import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

# Connect to Tor network
with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    controller.signal(Signal.NEWNYM)

# Define the search query
query = "usernames/passwords"

# Search the dark web
url = f"http://3g2upl4pq6kufc4m.onion/search?q={query}"
response = requests.get(url, proxies={'http': 'socks5://localhost:9050', 'https': 'socks5://localhost:9050'})
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the results
results = soup.find_all('div', class_='result')
for result in results:
    title = result.find('h3').text
    link = result.find('a')['href']
    print(f"Title: {title}")
    print(f"Link: {link}")