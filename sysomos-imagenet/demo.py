
import os
import sys

from clarifai.client import ClarifaiApi
#import caffenet as caffe
import download

import pprint

from apiclient.discovery import build


def get_clarifai_api_result(imageurl):
    return clarifaiApi.tag_image_urls(imageurl)

def get_google_api_result(imageurl):
    service = build("customsearch", "v1",
            developerKey="AIzaSyDiXTs1EgtxyksBV-lCXJ7L1Ttxci_DaZE")

    res = service.cse().list(
      q='lectures',
      searchType = "image",
    ).execute()
    pprint.pprint(res)

def get_caffe_result(imageurl):
    local_path = download.get(imageurl)
    return 1
    #caffe_response = caffe.classify(local_path)
    #return clarifaiApi.tag_image_urls(imageurl)

def main(argv):
    imageurl = argv[0]
    
    clarifaiApi = ClarifaiApi()

    if imageurl.startswith('http'):
        # get response from clarifaiApi
        clarifai_response = get_clarifai_api_result(imageurl)
        
        # get response from google image
        google_response = get_google_api_result(imageurl)
        
        # download the image and get result from caffe
        caffe_response = get_caffe_result(imageurl)

    elif os.path.isfile(imageurl):
        with open(imageurl,'rb') as image_file:
            response = api.tag_images(image_file)
    else:
        raise Exception("Invalid input")

    print(response)

if __name__ == '__main__':
    # main(sys.argv)
    get_google_api_result("saqwed")