from pymongo import MongoClient

def get(url):
    """
    Read the key value from mongo

    :param url:
    :return:
    """
    return MongoClient().sysomos.imageclass.find_one({'_id':url})['class']

def put(url, path, obj):
    """
    Write the key value to mongo

    :param url:
    :param obj:
    :return:
    """
    return MongoClient().sysomos.imageclass.update({'_id':url, 'path':path, 'class':obj})
