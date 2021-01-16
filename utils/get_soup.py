import requests
from bs4 import BeautifulSoup

HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'}


def get_soup(url):
    page = requests.get(url, headers=HEADER)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup, page.content
