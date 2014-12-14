# coding=utf-8
from urllib import urlretrieve
from base64 import b64encode
from logging import getLogger

base_path = "/root/.sysomos-imagenet/"
image_ext = {"jpeg", "jpg", "png"}

LOG = getLogger("downloader")

def image(url):
    ext = url.split(".")[-1].lower()
    if is_image(ext):
        LOG.info("File is an image with extension: " + ext)
        path = download_image(url, ext)
        return path
    else:
        LOG.info("File is not an image! Extension: " + ext)
        return None

def download_image(url, ext):
    path = base_path + b64encode(url) + "." + ext
    urlretrieve(url, path)
    LOG.info("File has been saved successfully! Path: " + path )
    return path

def is_image(ext):
    return (ext in image_ext)
