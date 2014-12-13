flask-image-classifier-service
==============================

This serves as both a proposal and a spec for the the hackathon project that we intend on building as part of Sysomos's first ever hackathon. The intention is to expose the Python-Caffe image classification api through Flask-Rest

### Success for this project is defined by implementing the following capabilities
  
```
app.py          - flask.app() interface must accept post requests and call orchestrator.py
orchestrator.py - controls cache, download, proprocess, caffenet, should be wrapped by @lru_mem_cache
db.py        - calls MongoDB to see if image_url exists and pulls out the classification object
download.py     - accepts image_url and downloads image into a directory, afterwards it will pass the path_to_downloaded_file     into preprocess.py
preprocess.py   - preprocesses the image and prepares for caffe ingestion
caffenet.py     - classifies and returns classification object
```

### Extensions should time allow

```
preprocess.py   - Potentially design on our own windowing functions
db.py        - Instead of caching only URL, cache on image fingerprint (for some definition of fingerprint)
orchestrator.py - multiprocessing on celery for concurrency
app.py          - expose tesseract api for optical character recogition
```
