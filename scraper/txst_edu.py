import requests
from bs4 import BeautifulSoup


def scrape_txst_edu(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    programs = []
    for item in soup.select('.scholarship-entry'):
        title = item.select_one('.scholarship-title').get_text(strip=True)
        link = item.select_one('a')['href']
        program_type = item.select_one('.scholarship-type').get_text(strip=True) if item.select_one(
            '.scholarship-type') else 'N/A'
        level = item.select_one('.scholarship-level').get_text(strip=True) if item.select_one(
            '.scholarship-level') else 'N/A'
        field = item.select_one('.scholarship-field').get_text(strip=True) if item.select_one(
            '.scholarship-field') else 'N/A'

        programs.append({
            'title': title,
            'link': link,
            'type': program_type,
            'level': level,
            'field': field
        })

    return programs
