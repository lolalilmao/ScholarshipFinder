import requests
from bs4 import BeautifulSoup


def scrape_goabroad_com(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    programs = []
    for item in soup.select('.program-item'):
        title = item.select_one('.program-title').get_text(strip=True)
        link = item.select_one('a')['href']
        program_type = item.select_one('.program-type').get_text(strip=True) if item.select_one(
            '.program-type') else 'N/A'
        level = item.select_one('.program-level').get_text(strip=True) if item.select_one('.program-level') else 'N/A'
        field = item.select_one('.program-field').get_text(strip=True) if item.select_one('.program-field') else 'N/A'

        programs.append({
            'title': title,
            'link': link,
            'type': program_type,
            'level': level,
            'field': field
        })

    return programs
