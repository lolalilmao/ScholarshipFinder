import requests
from bs4 import BeautifulSoup


def scrape_gooverseas_com(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    programs = []
    for item in soup.select('.study-abroad-item'):
        title = item.select_one('.study-abroad-title').get_text(strip=True)
        link = item.select_one('a')['href']
        program_type = item.select_one('.study-abroad-type').get_text(strip=True) if item.select_one(
            '.study-abroad-type') else 'N/A'
        level = item.select_one('.study-abroad-level').get_text(strip=True) if item.select_one(
            '.study-abroad-level') else 'N/A'
        field = item.select_one('.study-abroad-field').get_text(strip=True) if item.select_one(
            '.study-abroad-field') else 'N/A'

        programs.append({
            'title': title,
            'link': link,
            'type': program_type,
            'level': level,
            'field': field
        })

    return programs
