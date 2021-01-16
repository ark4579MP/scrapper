import os
import csv

from .get_catagories import get_catagories
from .get_products import get_products
from .process_products import process_products


def evselectro(save=True, refresh=False, dl=1):
    dir_ = 'data/evselectro'
    dir_products = dir_ + '/products'

    process_products(dir_=dir_, dl=dl)
