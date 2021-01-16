import os
import csv
from models.catagory import Catagory
from utils.catagory_utils import read_catagories, write_catagories
from utils.get_soup import get_soup


def get_catagories(save=True, dir_=None, refresh=False, dl=2):
    catgories_csv_name = '%s/catagories.csv' % dir_

    URL = 'https://www.evselectro.com/'

    if not refresh:
        read_catagories(dir_=dir_, dl=dl)

    if dl >= 1:
        print("Getting Catagories...")

    if dl >= 2:
        print("getting soup for %s" % (URL))
    soup, _html = get_soup(URL)
    if dl >= 2:
        print("got soup,")

    accordion = soup.find('ul', class_='accordion')

    accordion_links = accordion.find_all('a')

    catagories = []

    for link in accordion_links:
        _href = link['href']
        if(_href.startswith(URL)):
            _txt = link.text.strip()
            full_name = _href.split(URL)[1].replace('/', '_')

            c = Catagory(name=_txt, url=_href, full_name=full_name)
            catagories.append(c)

    if save and catagories:
        write_catagories(dir_=dir_, catagories=catagories, dl=dl)

    return catagories
