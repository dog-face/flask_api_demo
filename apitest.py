#!/usr/bin/python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "demo API -- available methods:<br/>/hello/<br/>/hello?name=&ltyourname&gt<br/>/hello/&ltyourname&gt"

@app.route('/hello/')
def respond_hello():
    name = request.args.get('name')
    if name is not None:
        return "Hello %s" % name
    else:
        return "Hello to you too."

@app.route('/hello/<string:name>')
def respond_your_name(name):
    return "Hello %s" % name

if __name__ == '__main__':
    #context = ('etc/letsencrypt/live/server.mznco.net/cert.pem', '/etc/letsencrypt/live/server.mznco.net/privkey.pem'
    #app.run(debug=True, ssl_context=context)
    app.run(debug=True)

