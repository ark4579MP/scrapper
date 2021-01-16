from models.catagory import Catagory
from utils.catagory_utils import read_catagories, write_catagories
from utils.get_soup import get_soup


def get_catagories(dir_=None, save=True, refresh=False, dl=2):
    # if not refresh:
    #     catagories = read_catagories(dir_=dir_, dl=dl)
    #     if catagories:
    #         return catagories

    BASE_URL = 'https://w11stop.com'
    URL = BASE_URL+'/index.php?route=common/home'
    soup, _html = get_soup(url=URL)

    if dl >= 2:
        print("Getting catagories...")

    ul_elements = soup.find('div', class_='grid-rows')

    ul_links = []
    for ul_element in ul_elements:
        ul_element_links = ul_element.find_all('a')
        for ul_link in ul_element_links:
            ul_links.append(ul_link)

    catagories = []

    for ul_link in ul_links:
        # if dl >= 4:
        #     print(ul_link)

        name = ul_link.text.strip()
        link = ul_link.get('href')
        if not link:
            # print("skipping", ul_link)
            continue
        full_name = link.split(BASE_URL+"/")[1]

        c = Catagory(name=name, url=link, full_name=full_name)

        # if dl >= 3:
        #     print(c)

        catagories.append(c)

    write_catagories(dir_=dir_, catagories=catagories, dl=dl)

    return catagories
