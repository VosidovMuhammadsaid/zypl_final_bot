import os
import sys
sys.path.append('/usr/local/lib/python3.10/dist-packages')
from flask import Flask
app = Flask(__name__)
application = app
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()