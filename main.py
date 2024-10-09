import requests
from bs4 import BeautifulSoup
import logging

GITHUB_URL = 'https://github.com'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'

logging.basicConfig(level=logging.INFO)

def get_repositories(username: str) -> list:
    """
    Scrape a GitHub account and make list of their repositories 
    """
    url = f'{GITHUB_URL}/{usa ername}?tab=repositories'
    try:
        response = requests.get(url, headers={'User -Agent': USER_AGENT})
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    except requests.RequestException as e:
        logging.error(f'Error fetching repositories: {e}')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    repositories = []
    for repo_li in soup.select('li.col-12.d-flex.flex-justify-between.width-full.py-4.border-bottom.color-border-muted.public.source'):
        repo_data = {}
        repo_data['Repositories'] = repo_li.find('h3.wb-break-all').get_text(strip=True)
        repo_data['link_repo'] = GITHUB_URL + repo_li.find('a')['href']
        repo_data['Description'] = repo_li.find('p.col-9.d-inline-block.color-fg-muted.mb-2.pr-4').get_text(strip=True) if repo_li.find('p.col-9.d-inline-block.color-fg-muted.mb-2.pr-4') else None
        repositories.append(repo_data)
    return repositories

def main():
    username = input('Enter your GitHub username: ')
    repositories = get_repositories(username)
    logging.info(f'Repositories for {username}:')
    for repo in repositories:
        logging.info(f"  {repo['Repositories']} - {repo['link_repo']} - {repo['Description']}")

if __name__ == '__main__':
    main()
