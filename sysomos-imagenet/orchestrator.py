# coding=utf-8
from functools32 import lru_cache

import db
import preprocess
import download
import caffenet


@lru_cache(maxsize=1024)
def run(url):
    """
    Consume a url and orchestrates the classification process

    :param url:
    :return: classification object
    """
    path_to_file = download.get(url)
    retresult = caffenet.classify(path_to_file)
    return retresult
