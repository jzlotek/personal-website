#!/bin/sh

(sass --watch static/scss:static/css &)
(python app.py --debug)

wait
