import os
import csv
from models.product import Product
from utils.get_soup import get_soup


def get_products(catagory=None, limit=100, save=False, dir_=None, refresh=False, dl=2):
    if not catagory:
        return
    catagory_products_csv_name = '%s/products/%s.csv' % (
        dir_, catagory.full_name)

    if not refresh and os.path.isfile(catagory_products_csv_name):
        print('skipping %s because %s already exists!' %
              (catagory.name, catagory_products_csv_name))
        products = []
        with open(catagory_products_csv_name) as f:
            csv_reader = csv.reader(f)
            csv_rows = []
            for row in csv_reader:
                csv_rows.append(row)
            csv_rows = csv_rows[1:]
            for row in csv_rows:
                p = Product(_csv=row)
                products.append(p)
        return products

    URL = '%s?limit=%d' % (catagory.url, limit)

    if dl >= 2:
        print("getting soup for %s because %s not found!" %
              (URL, catagory_products_csv_name))
    soup, _html = get_soup(URL)
    results = soup.find_all('div', class_='product')

    products = []
    for r in results:
        url = r.find('a')['href']
        name = r.find('div', class_='name').find('a').text.strip()
        price = r.find('div', class_='price').text.strip()

        p = Product(name=name, price=price, url=url)

        products.append(p)

    if save:
        dir_products = '%s/products' % dir_

        if not os.path.exists(dir_products):
            os.makedirs(dir_products)

        catagory_rows = [(Product()).to_csv_header()]
        catagory_rows += [p.to_csv_row() for p in products]

        print('saving %s' % (catagory_products_csv_name))
        with open(catagory_products_csv_name, 'w', newline='', encoding="utf-8") as f:
            csv_writter = csv.writer(f)
            csv_writter.writerows(catagory_rows)

    return products
