# coding=utf-8
import numpy
import sys
import pandas as pd
import caffe
import time
from config import CAFFE_PATH

def classify(prepared_image):
    """
    Consume a image and return the classfication

    :param prepared_image:
    :return: classification object
    """
    MODEL_FILE = CAFFE_PATH + '/models/bvlc_reference_caffenet/deploy.prototxt'
    PRETRAINED = CAFFE_PATH + '/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
    LABEL_FILE = CAFFE_PATH + '/data/ilsvrc12/synset_words.txt'
    classifier = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=numpy.load(CAFFE_PATH + '/caffe/imagenet/ilsvrc_2012_mean.npy'),
                       channel_swap=(2,1,0),
                       raw_scale=255,
                       image_dims=(256, 256))
    classifier.set_phase_test()
    classifier.set_mode_cpu()
    input_image = caffe.io.load_image(prepared_image)
    # Classify
    start = time.time()
    scores = classifier.predict(input_image).flatten()
    print "Done in %.2f s." % (time.time() - start)

    with open(LABEL_FILE) as f:
      labels_df = pd.DataFrame([
           {
               'synset_id': l.strip().split(' ')[0],
               'name': ' '.join(l.strip().split(' ')[1:]).split(',')[0]
           }
           for l in f.readlines()
        ])
    labels = labels_df.sort('synset_id')['name'].values

    indices = (-scores).argsort()[:5]
    predictions = labels[indices]

    meta = [
               (p, '%.5f' % scores[i])
               for i, p in zip(indices, predictions)
           ]

    print meta
    return {'class':'cat', 'confidence':1}

if __name__ == '__main__':
    classify(sys.argv[1])