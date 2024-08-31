import requests
from bs4 import BeautifulSoup


def scrape_universities_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    universities = []
    for item in soup.select('.university-name'):  # Убедитесь, что класс правильный
        name = item.get_text()
        universities.append(name)

    return universities


def scrape_programs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    programs = []
    for item in soup.select('.program-class'):  # Убедитесь, что класс правильный
        title = item.select_one('.title-class').get_text()
        link = item.select_one('a')['href']
        programs.append({'title': title, 'link': link})

    return programs
