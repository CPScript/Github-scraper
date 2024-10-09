## How it Works
* The script sends a GET request to the GitHub user page and parses the HTML content using BeautifulSoup.
* It extracts the repository names, links, and descriptions from the HTML content.
* The script then asks the user if they want to download all the repositories.
* If the user chooses to download all repositories, the script creates a directory with the username as the name and clones each repository into that directory using `git clone`.

## Installation
* Clone the repo: `git clone https://github.com/CPScript/Github-scraper.git`
* install requirements: `python setup.py`
* execute the script: `python main.py`

> WARNING: This script still scrapes GitHub's website, which may be against their terms of service. Additionally, the script may break if GitHub changes their HTML structure or adds anti-scraping measures.
