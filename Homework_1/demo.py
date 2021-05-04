from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods = ['GET'])

def home():
    return ('<html><head><title></title></head><body><h1>Hello World</h1></body></html>')

if __name__ == '__main__':
    app.run(port = 5000, debug = True)