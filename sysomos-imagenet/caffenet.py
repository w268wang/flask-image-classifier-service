# coding=utf-8
import numpy
import sys
import pandas as pd
import caffe
import time

CAFFE_PATH = '/home/vagrant/caffe'

def classify(prepared_image):
    """
    Consume a image and return the classfication

    :param prepared_image:
    :return: classification object
    """
    MODEL_FILE = CAFFE_PATH + '/models/bvlc_reference_caffenet/deploy.prototxt'
    PRETRAINED = CAFFE_PATH + '/models/bvlc_reference_caffenet/bvlc_reference_caffenet.caffemodel'
    LABEL_FILE = CAFFE_PATH + '/data/ilsvrc12/synset_words.txt'
    # MODEL_FILE = CAFFE_PATH + '/examples/imagenet/imagenet_deploy.prototxt'
    # PRETRAINED = CAFFE_PATH + '/examples/imagenet/caffe_reference_imagenet_model'
    # LABEL_FILE = CAFFE_PATH + '/data/ilsvrc12/synset_words.txt'
    MEAN_FILE = CAFFE_PATH + '/python/caffe/imagenet/ilsvrc_2012_mean.npy'
    classifier = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean_file=MEAN_FILE,channel_swap=(2,1,0),input_scale=255,image_dims=(256,256),gpu=False)
    classifier.set_phase_test()
    classifier.set_mode_cpu()
    input_image = [caffe.io.load_image(prepared_image)]
    # Classify
    start = time.time()
    scores = classifier.predict(input_image, False).flatten()
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
