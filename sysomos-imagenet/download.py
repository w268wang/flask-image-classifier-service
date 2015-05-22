# coding=utf-8
from urllib import urlretrieve
from base64 import b64encode

base_path = "/root/.sysomos-imagenet/"
image_ext = {"jpeg", "jpg", "png"}


def get(url):
    ext = url.split(".")[-1].lower()
    if ext not in image_ext:
        return download_image(url, ext)


def download_image(url, ext):
    path = base_path + b64encode(url) + "." + ext
    urlretrieve(url, path)
    return path
