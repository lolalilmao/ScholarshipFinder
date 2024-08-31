import pandas as pd
from scraper.gradschools_com import scrape_gradschools_com
from scraper.scholarships_com import scrape_scholarships_com
from scraper.bold_org import scrape_bold_org
from scraper.sparxmaths_com import scrape_sparxmaths_com
from scraper.txst_edu import scrape_txst_edu
from scraper.fellowshipbard_com import scrape_fellowshipbard_com
from scraper.scholarshipdb_net import scrape_scholarshipdb_net
from scraper.gooverseas_com import scrape_gooverseas_com
from scraper.goabroad_com import scrape_goabroad_com
from scraper.intostudy_com import scrape_intostudy_com


def scrape_all_sites():
    all_programs = []
    urls = [
        "https://www.gradschools.com",
        "https://www.scholarships.com",
        "https://bold.org",
        "https://sparxmaths.com",
        "https://txst.edu",
        "https://fellowshipbard.com",
        "https://scholarshipdb.net",
        "https://www.gooverseas.com/study-abroad",
        "https://www.goabroad.com/study-abroad",
        "https://www.intostudy.com/en/study-abroad"
    ]

    for url in urls:
        try:
            print(f"Scraping data from {url}")
            if "gradschools.com" in url:
                programs = scrape_gradschools_com(url)
            elif "scholarships.com" in url:
                programs = scrape_scholarships_com(url)
            elif "bold.org" in url:
                programs = scrape_bold_org(url)
            elif "sparxmaths.com" in url:
                programs = scrape_sparxmaths_com(url)
            elif "txst.edu" in url:
                programs = scrape_txst_edu(url)
            elif "fellowshipbard.com" in url:
                programs = scrape_fellowshipbard_com(url)
            elif "scholarshipdb.net" in url:
                programs = scrape_scholarshipdb_net(url)
            elif "gooverseas.com" in url:
                programs = scrape_gooverseas_com(url)
            elif "goabroad.com" in url:
                programs = scrape_goabroad_com(url)
            elif "intostudy.com" in url:
                programs = scrape_intostudy_com(url)
            else:
                programs = []

            all_programs.extend(programs)
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    print(f"Total programs scraped: {len(all_programs)}")
    return all_programs


def filter_programs(programs, criteria):
    filtered_programs = []
    for program in programs:
        if all(
                program.get(key) in value if isinstance(value, list) else program.get(key) == value
                for key, value in criteria.items()
        ):
            filtered_programs.append(program)
    return filtered_programs


def main():
    # Сбор данных с сайтов
    programs = scrape_all_sites()

    # Пример критериев
    criteria = {
        'type': 'Full Scholarship',
        'level': 'Master\'s',
        'field': ['Economics', 'Political Science']
    }

    # Фильтрация данных
    filtered_programs = filter_programs(programs, criteria)

    # Вывод в таблицу
    df = pd.DataFrame(filtered_programs)
    df.to_csv('filtered_programs.csv', index=False)

    print(f"Filtered programs saved to 'filtered_programs.csv'")
    print(df)


if __name__ == "__main__":
    main()
