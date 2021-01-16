from models.catagory import Catagory
from utils.get_soup import get_soup


def get_catagories(dir_=None, save=True, refresh=False, dl=2):
    BASE_URL = 'https://w11stop.com'
    URL = BASE_URL+'/index.php?route=common/home'
    soup, _html = get_soup(url=URL)

    ul_elements = soup.find('div', class_='grid-rows')

    ul_links = []
    for ul_element in ul_elements:
        ul_element_links = ul_element.find_all('a')
        for ul_link in ul_element_links:
            ul_links.append(ul_link)

    catagories = []

    for ul_link in ul_links:
        name = ul_link.text
        link = ul_link['href']
        full_name = link.split(BASE_URL+"/")

        c = Catagory(name=name, url=link, full_name=full_name)

        catagories.append(c)

    return catagories
