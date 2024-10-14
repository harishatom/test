from flask import Flask
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.get("/")
def hello_world():
    '''Default route'''
    return "<p>Hello, World!</p>"

@app.get("/hello/<name>")
def hello(name: str):
    '''Route with parameter'''
    return f"Hello, {escape(name)}!"

@app.post("/sample-post-greeting")
def sample_post_greeting():
    '''Sample POST greeting'''
    return f"Hello, {request.json['name']}!"


