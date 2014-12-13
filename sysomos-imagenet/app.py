# coding=utf-8

from flask import Flask
import orchestrator

app = Flask(__name__)

@app.route('/classify')
def classify():
    """
    Accept post request and run orchestration

    :return: classification object
    """
    url = "jasonliu.rocks/static/swag.jpg"
    return orchestrator.run(url)

if __name__ == '__main__':
    app.run()