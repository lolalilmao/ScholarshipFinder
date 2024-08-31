import requests
from bs4 import BeautifulSoup


def scrape_scholarshipdb_net(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    scholarships = []
    for item in soup.select('.scholarship-item'):  # Замените на правильные селекторы
        title = item.select_one('.scholarship-title').get_text(strip=True)
        description = item.select_one('.scholarship-description').get_text(strip=True)
        link = item.select_one('a')['href']
        scholarships.append({'title': title, 'description': description, 'link': link})

    return scholarships
