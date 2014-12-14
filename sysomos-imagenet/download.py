# coding=utf-8

def image(url):
    if is_image(url):
        path = download_image(url)
        return path
    else:
        return None

def download_image(url):
    return None

def is_image(url):
    return None