from __future__ import annotations

import argparse
import datetime
import glob
import random
from dataclasses import dataclass
from typing import Dict
from pathlib import PosixPath

import markdown2
import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.cors import CORSMiddleware

BUILD_DATE: str = (
    datetime.datetime.now().astimezone().strftime("%a, %d %b %Y %H:%M:%S %Z")
)


if PosixPath("/tmp/build_date").exists():
    BUILD_DATE = PosixPath("/tmp/build_date").read_text().strip()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

POSTS: Dict[str, Post] = {}
FMT_STR = "%Y%m%d"


@dataclass
class Post:
    html: str
    rss: str
    path: str
    title: str
    date: str
    words: int
    pub_date: str
    tags: set[str]


def load_posts(directory):
    for file in glob.glob(f"{directory}/*.md"):
        file_name = file.split("/")[-1]
        dt = datetime.datetime.strptime(file_name[:8], FMT_STR).astimezone()
        title = list(filter(lambda x: x != "", file_name[8:].split(".")[0].split("_")))
        slug = "-".join(title)
        path = f"{dt.year}/{dt.month}/{dt.day}/{slug.lower()}"
        mkdown: markdown2.Markdown = markdown2.markdown_path(
            file, extras=["fenced-code-blocks", "metadata", "code-friendly"]
        )
        html = str(mkdown)
        rss = str(markdown2.markdown_path(file, extras=["metadata"]))
        split_date = path.split("/")[:-1]
        POSTS[path] = Post(
            html=html,
            rss=rss,
            path=path,
            title=" ".join(title),
            date=".".join(split_date),
            words=len(html.split()),
            pub_date=dt.strftime("%a, %d %b %Y %H:%M:%S %Z"),
            tags=set(mkdown.metadata.get("tags", [])),
        )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/projects", response_class=HTMLResponse)
async def projects(request: Request):
    return templates.TemplateResponse("projects.html", {"request": request})


@app.get("/donate", response_class=HTMLResponse)
async def donate(request: Request):
    return templates.TemplateResponse("donate.html", {"request": request})


@app.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    return templates.TemplateResponse("blog.html", {"posts": POSTS, "request": request})


@app.get("/rss")
async def rss(request: Request):
    return templates.TemplateResponse(
        "rss.html",
        {"posts": POSTS, "build_date": BUILD_DATE, "request": request},
        media_type="application/xml",
        headers={
            "Accept-Range": "bytes",
            "Connection": "Keep-Alive",
            "Keep-Alive": "timeout=5, max=100",
        },
    )


@app.get("/blog/{year}/{month}/{day}/{title}", response_class=HTMLResponse)
async def blog_post(year: int, month: int, day: int, title: str, request: Request):
    path = f"{year}/{month}/{day}/{title}"
    if path not in POSTS:
        raise HTTPException(status_code=404)
    return templates.TemplateResponse(
        "post.html", {"post": POSTS.get(path), "request": request}
    )


@app.exception_handler(StarletteHTTPException)
@app.exception_handler(HTTPException)
async def exception_handler(request: Request, exc):
    if random.randint(0, 50) != 0:
        return templates.TemplateResponse(
            "404.html", {"request": request}, status_code=404
        )
    else:  # unlucky
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="Port to use", default=5000, type=int)
    parser.add_argument("--posts", help="Directory to load posts from", default="posts")
    parser.add_argument(
        "--debug", help="Enables auto reload", default=False, action="store_true"
    )
    return parser.parse_args()


# bootstrap args and posts
args = parse_args()
load_posts(args.posts)


def main():
    uvicorn.run(
        app, host="0.0.0.0", port=args.port, forwarded_allow_ips="*", proxy_headers=True
    )


if __name__ == "__main__":
    main()
