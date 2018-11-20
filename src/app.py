from flask import Flask, render_template, jsonify
import requests
import bs4
import json
import re
import datetime
import multiprocessing
import os
from python.tms_crawler import Crawler

def run_crawler(crawler):
    try:
        crawler.crawl()
    except Exception as e:
        print("\n{}\n\n{}\n".format(str(e.message), str(datetime.datetime.now())))

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/output.json')
def get_output():
    return app.response_class(
        response="".join(open('./output.json', 'r').readlines()),
        mimetype='application/json'
    )

if __name__ == '__main__':
    
    crawler = Crawler()

    crawler_process = multiprocessing.Process(target=run_crawler, args=[crawler])
    crawler_process.start()

    if '.tmp' not in os.listdir('./'):
        os.mkdir('./.tmp')

    try:
        app.run()
    except Exception as e:
        crawler_process.terminate()