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
    retresult = db.get(url)
    if not retresult:
        path_to_file = download.image(url)
        prepared_obj = preprocess.prepare_image(path_to_file)
        retresult = caffenet.classify(prepared_obj)
        db.put(url, path_to_file, retresult)
    return retresult
