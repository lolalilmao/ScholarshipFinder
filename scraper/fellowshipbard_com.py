import requests
from bs4 import BeautifulSoup


def scrape_fellowshipbard_com(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    programs = []
    for item in soup.select('.fellowship-item'):
        title = item.select_one('.fellowship-title').get_text(strip=True)
        link = item.select_one('a')['href']
        program_type = item.select_one('.fellowship-type').get_text(strip=True) if item.select_one(
            '.fellowship-type') else 'N/A'
        level = item.select_one('.fellowship-level').get_text(strip=True) if item.select_one(
            '.fellowship-level') else 'N/A'
        field = item.select_one('.fellowship-field').get_text(strip=True) if item.select_one(
            '.fellowship-field') else 'N/A'

        programs.append({
            'title': title,
            'link': link,
            'type': program_type,
            'level': level,
            'field': field
        })

    return programs
