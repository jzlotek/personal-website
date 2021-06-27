import argparse
import datetime
import glob
import os
import markdown2

from flask import Flask, request, send_file, render_template, redirect, abort

app = Flask(__name__, static_folder='static', static_url_path='', template_folder='templates')


POSTS = {}


def load_posts(directory):
    FMT_STR = '%Y%m%d'
    for file in glob.glob(f'{directory}/*.md'):
        file_name = file.split('/')[-1]
        dt = datetime.datetime.strptime(file_name[:8], FMT_STR)
        title = list(filter(lambda x: x != '', file_name[8:].split('.')[0].split('_')))
        slug = '-'.join(title)
        path = f'{dt.year}/{dt.month}/{dt.day}/{slug.lower()}'
        POSTS[path] = {
            "html": str(markdown2.markdown_path(file)),
            "title": ' '.join(title),
            "date": '.'.join(path.split('/')[:-1])
        }


@app.route('/static/<path:path>')
def get_static_resource(path):
    return send_file(os.path.join(app.root_path, 'static', path))


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/projects')
def projects():
    return render_template('projects.html')


@app.get('/blog')
def blog():
    return render_template('blog.html', posts=POSTS)


@app.get('/blog/<path:path>')
def blog_post(path):
    if path not in POSTS:
        return abort(404)
    return render_template('post.html', last=request.referrer, post=POSTS.get(path))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', help="Port to use", default=5000)
    parser.add_argument('--posts', help='Directory to load posts from', default='posts')
    parser.add_argument('--debug', help='Enables auto reload', default=False, action='store_true')
    return parser.parse_args()


# bootstrap args and posts
args = parse_args()
load_posts(args.posts)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=args.port, debug=args.debug)

