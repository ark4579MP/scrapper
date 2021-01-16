import os
import csv
from models.catagory import Catagory
from utils.get_soup import get_soup


def get_catagories(save=True, dir_=None, refresh=False, dl=2):
    catgories_csv_name = '%s/catagories.csv' % dir_

    URL = 'https://www.evselectro.com/'

    if not refresh and os.path.isfile(catgories_csv_name):
        if dl >= 2:
            print("skipping fetching catagories because %s already exists" %
                  (catgories_csv_name))
        with open(catgories_csv_name, encoding="utf-8") as f:
            csv_reader = csv.reader(f)
            csv_rows = []
            for row in csv_reader:
                csv_rows.append(row)
            csv_rows = csv_rows[1:]
            catagories = [Catagory(_csv=c) for c in csv_rows]
            return catagories
        return

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
        catagories_row = [catagories[0].to_csv_header()]
        catagories_row += [c.to_csv_row() for c in catagories]

        with open(catgories_csv_name, 'w', newline='', encoding="utf-8") as f:
            csv_writter = csv.writer(f)
            csv_writter.writerows(catagories_row)

    return catagories
