import requests
from bs4 import BeautifulSoup


def scrape_gradschools_com(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    programs = []
    for item in soup.select('.program-item'):  # Замените на правильные селекторы
        title = item.select_one('.program-title').get_text(strip=True)
        link = item.select_one('a')['href']
        programs.append({'title': title, 'link': link})

    return programs
