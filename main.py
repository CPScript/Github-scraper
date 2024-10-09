import requests
from bs4 import BeautifulSoup
import logging
import os
import subprocess

GITHUB_URL = 'https://github.com'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0'

logging.basicConfig(level=logging.INFO)

def get_repositories(username: str) -> list:
    """
    Scrape a github account and make a list of their repositories
    """
    url = f'{GITHUB_URL}/{username}?tab=repositories'
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

def clone_repositories(repositories: list, username: str) -> None:
    """
    Clone all repositories in the given list to a directory with the username
    """
    dir_name = username
    dir_path = os.path.join(os.getcwd(), dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for repo in repositories:
        repo_name = repo['Repositories']
        repo_url = repo['link_repo']
        repo_dir = os.path.join(dir_path, repo_name)
        if not os.path.exists(repo_dir):
            logging.info(f'Cloning {repo_name}...')
            subprocess.run(['git', 'clone', repo_url, repo_dir])
            logging.info(f'Cloned {repo_name} to {repo_dir}')
        else:
            logging.info(f'Skipping {repo_name} - already cloned')

def main():
    username = input('Enter your GitHub username: ')
    repositories = get_repositories(username)
    logging.info(f'Repositories for {username}:')
    for repo in repositories:
        logging.info(f"  {repo['Repositories']} - {repo['link_repo']} - {repo['Description']}")

    download_all = input('Do you want to download all repositories? (y/n): ')
    if download_all.lower() == 'y':
        clone_repositories(repositories, username)

if __name__ == '__main__':
    main()
