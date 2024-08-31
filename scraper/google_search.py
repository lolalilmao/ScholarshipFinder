import requests
from bs4 import BeautifulSoup
import urllib.parse


def search_google(query):
    search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    response = requests.get(search_url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for a in soup.select('a'):
        href = a.get('href')
        if href and 'url?q=' in href:
            link = href.split('url?q=')[1].split('&')[0]
            links.append(link)

    return links
