import requests
from bs4 import BeautifulSoup
import re

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Paste Sources Twitter list URL
paste_sources_url = "https://twitter.com/i/lists/203915919/members"

# Function to scrape usernames and passwords from Paste sites
def scrape_paste_sites():
    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get the list of Paste Sources Twitter accounts
    paste_sources = api.list_members("203915919", "members")

    for user in paste_sources:
        # Get the user's latest tweets
        tweets = api.user_timeline(screen_name=user.screen_name, count=10)
        for tweet in tweets:
            # Check if the tweet contains a link to a Paste site
            if "pastebin.com" in tweet.text or "paste.ee" in tweet.text or "paste.org" in tweet.text:
                # Scrape the Paste site for usernames and passwords
                paste_url = re.search(r"(https?://\S+)", tweet.text).group(1)
                response = requests.get(paste_url)
                soup = BeautifulSoup(response.text, "html.parser")
                for line in soup.get_text().split("\n"):
                    if ":" in line:
                        username, password = line.split(":")
                        print(f"Username: {username.strip()}, Password: {password.strip()}")

# Call the scrape_paste_sites function to start the script
scrape_paste_sites()
