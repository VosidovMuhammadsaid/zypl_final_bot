import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from PIL import Image


app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['front']
    img = Image.open(file.stream)
    img.save("img/front.png")

    file1 = request.files['back']
    img1 = Image.open(file1.stream)
    img1.save("img/back.png")
    return jsonify({'msg1': 'success1', 'size1': [img1.width, img1.height]},
                   {'msg':'success', 'size':[img.width, img.height]})


if __name__ == "__main__":
    app.run(debug=True)