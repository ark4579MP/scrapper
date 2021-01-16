import os
import csv
from .get_catagories import get_catagories
from .get_products import get_products


def process_products(dir_=None, dl=2):
    process_products_csv_name = '%s/all_products.csv' % (dir_)

    if dl >= 1:
        print("Processing Products...")

    if os.path.isfile(process_products_csv_name):
        if dl >= 3:
            print("skipping processing of products because %s already exists!" %
                  (process_products_csv_name))
        return

    categories = get_catagories(dir_=dir_)

    all_products = []
    for catagory in categories:
        catagory_products = get_products(catagory=catagory, dir_=dir_)
        for p in catagory_products:
            p.catagory = catagory
        all_products += catagory_products

    fields = ['name', 'price', 'url', 'catagory_name',
              'catagory_full_name', 'catagory_url']
    p_values = [p.get_values(fields) for p in all_products]

    with open(process_products_csv_name, 'w', newline='', encoding='utf-8') as f:
        csv_writter = csv.writer(f)
        csv_writter.writerow(fields)
        csv_writter.writerows(p_values)
