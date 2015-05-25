
import os
import sys

from clarifai.client import ClarifaiApi
#import caffenet as caffe
import download

import pprint

from apiclient.discovery import build


def get_clarifai_api_result(imageurl):
    clarifaiApi = ClarifaiApi()
    json_dic = clarifaiApi.tag_image_urls(imageurl)
    json_pair = json_dic["results"][0]["result"]["tag"]

    # extract information from the result
    classes_list = json_pair["classes"]
    probs_list = json_pair["probs"]
    result_pair = {}
    for i in xrange(len(classes_list)):
        result_pair[classes_list[i]] = probs_list[i]
    print(result_pair)
    return result_pair

def get_google_api_result(imageurl):
    #http://images.google.com/searchbyimage?site=search&image_url={user_url}
    service = build("customsearch", "v1",
            developerKey="AIzaSyDiXTs1EgtxyksBV-lCXJ7L1Ttxci_DaZE")

    res = service.cse().list(
      q='cat',
      image_url='http://hdwbin.com/wp-content/uploads/2015/01/Cute-Cat-picture.jpg',
      cx="005698134567108455978:fte4nd-jg5w",
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