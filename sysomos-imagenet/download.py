# coding=utf-8
from urllib import urlretrieve
from os.path import realpath
from base64 import b64encode
from logging import getLogger

base_path = "/root/.sysomos-imagenet/"
image_ext = {"jpeg", "jpg", "png"}

LOG = getLogger("downloader")

def image(url):
    ext = url.split(".")[-1].lower()
    if is_image(ext):
        LOG.info("File is an imagine with extension: " + ext)
        path = download_image(url, ext)
        return path
    else:
        LOG.info("File is not an imagine! Extension: " + ext)
        return None

def download_image(url, ext):
    path = base_path + b64encode(url) + "." + ext
    resource = urlretrieve(url, path)
    LOG.info("File has been saved successfully! Path: " + path )
    return path

def is_image(ext):
    return (ext in image_ext)

image("http://upload.wikimedia.org/wikipedia/commons/c/c9/FEMA_-_25380_-_Photograph_by_Barry_Bahler_taken_on_07-27-2006_in_District_of_Columbia.jpg")