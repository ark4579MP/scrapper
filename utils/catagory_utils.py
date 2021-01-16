import os
import csv
from models.catagory import Catagory


def write_catagories(dir_=None, catagories=None, dl=3):
    catgories_csv_name = '%s/catagories.csv' % dir_

    if not dir_ or not catagories:
        pass

    if not os.path.exists(dir_):
        os.mkdir(dir_)

    catagories_row = [catagories[0].to_csv_header()]
    catagories_row += [c.to_csv_row() for c in catagories]

    with open(catgories_csv_name, 'w', newline='', encoding="utf-8") as f:
        csv_writter = csv.writer(f)
        csv_writter.writerows(catagories_row)


def read_catagories(dir_=None, dl=3):
    catgories_csv_name = '%s/catagories.csv' % dir_

    if not dir_ or not os.path.isfile(catgories_csv_name):
        return

    if dl >= 3:
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
