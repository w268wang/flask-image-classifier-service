# coding=utf-8
from functools32 import lru_cache
import numpy
import sys
import pandas as pd
import caffe
import time

CAFFE_PATH = '/home/vagrant/caffe'
MODEL_FILE = CAFFE_PATH + '/models/bvlc_reference_caffenet/deploy.prototxt'
PRETRAINED = CAFFE_PATH + '/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
MEAN_FILE = CAFFE_PATH + '/python/caffe/imagenet/ilsvrc_2012_mean.npy'
LABEL_FILE = CAFFE_PATH + '/data/ilsvrc12/synset_words.txt'


@lru_cache(max=2)
def get_classifier():
    """
    obtain a cached classifier object

    :return: classifier
    """

    classifier = caffe.Classifier(
        MODEL_FILE, PRETRAINED,
        mean_file=MEAN_FILE,
        channel_swap=(2, 1, 0),
        input_scale=255,
        image_dims=(256, 256)
    )

    classifier.set_phase_test()
    classifier.set_mode_cpu()

    return classifier


@lru_cache(max=2)
def get_labels():
    """
    obtain labels from label file

    :return:
    """
    with open(LABEL_FILE) as f:
        labels_df = pd.DataFrame([
            {
                'synset_id': l.strip().split(' ')[0],
                'name': ' '.join(l.strip().split(' ')[1:]).split(',')[0]
            }
            for l in f.readlines()
        ])
    labels = labels_df.sort('synset_id')['name'].values
    return labels


@lru_cache(max=100)
def classify(prepared_image, top=5):
    """
    Consume a image and return the classfication

    :param prepared_image:
    :param top:
    :return: classification object
    """
    input_image = [caffe.io.load_image(prepared_image)]

    start_time = time.time()
    scores = get_classifier().predict(input_image, False).flatten()
    end_time = time.time()

    total_time = end_time - start_time

    indices = (-scores).argsort()[:top]
    predictions = get_labels()[indices]

    meta = [
        (p, '%.5f' % scores[i])
        for i, p in zip(indices, predictions)
    ]

    return dict(data=meta, time=total_time)


if __name__ == '__main__':
    classify(sys.argv[1])
