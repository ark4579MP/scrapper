from .get_catagories import get_catagories


def w11stop(save=True, refresh=False, dl=1):
    dir_ = 'data/w11stop'

    get_catagories(dir_=dir_, dl=dl)
