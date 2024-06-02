#!/usr/bin/env python

from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!\n"


@app.route('/sum')
def sum():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return "Sum of {0} and {1} is {2}\n".format(a, b, a+b)

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
