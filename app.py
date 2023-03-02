from flask import Flask, request, Response
import jsonpickle
import numpy as np
import cv2
from http.server import SimpleHTTPRequestHandler, HTTPServer
from readpass import read_passport
# from readpass_back import read_pass_back
import random
from zypl_encoder import zypl_encoder, zypl_decoder
from PIL import Image
from datetime import datetime



app = Flask(__name__)


@app.route('/')
def index():
    return "<center><h1>Demo zypl.pass</h1></center>"


@app.route('/-S101D1682Z442N1025', methods=['POST'])
def test1():
    rand_front = random.randint(1, 100000)

    f = open("counter.txt", "r")
    counters = f.read()
    f.close()
    counter = "NONE"
    countering = counters.split("\n")
    for i in countering:
        if "-S101D1682Z442N1025" in i:
            counter = int(i.split(":")[1])

    if counter == "NONE":
        return Response(response=jsonpickle.encode({"Error_message": "Failed on Authorization"}), status=200,
                        mimetype="application/json")
    if counter > 250:
        return Response(
            response=jsonpickle.encode({"Error_message": "Your subscription has been over (0 runs on the balance)."}),
            status=200, mimetype="application/json")

    f = open("counter.txt", "w")
    f.write(counters.replace("-S101D1682Z442N1025:" + str(counter), "-S101D1682Z442N1025:" + str(counter + 1)))
    f.close()

    nline = False
    try:
        f = open("Request_History/-S101D1682Z442N1025.txt", "r")
        txt = f.read()
        f.close()

        nline = True
    except:
        f = open("Request_History/-S101D1682Z442N1025.txt", "w")
        f.close()
        txt = ""

    file = request.files['front']
    img = Image.open(file.stream)
    img.save(f"uploads/front-{rand_front}.png")
    read = read_passport(f"uploads/front-{rand_front}.png")

    # file_back = request.files['back']
    # img_back = Image.open(file_back.stream)
    # img_back.save(f"uploads/back-{rand_front}.png")
    # read_back = read_pass_back(f"uploads/back-{rand_front}.png")

    response = {'Front': read}
    #, 'Back': read_back
    if nline:
        txt += "\n"
    txt += "img_id: front-" + str(rand_front) + ".png  count: " + str(counter) + "  time: " + str(datetime.now())
    txt += "img_id: back-" + str(rand_front) + ".png  count: " + str(counter) + "  time: " + str(datetime.now())
    f = open("Request_History/-S101D1682Z442N1025.txt", "w")
    f.write(txt)
    f.close()
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/-W485M530G1445F1226A2026', methods=['POST'])
def test2():
    rand_front = random.randint(1, 100000)

    f = open("counter.txt", "r")
    counters = f.read()
    f.close()
    counter = "NONE"
    countering = counters.split("\n")
    for i in countering:
        if "-W485M530G1445F1226A2026" in i:
            counter = int(i.split(":")[1])

    if counter == "NONE":
        return Response(response=jsonpickle.encode({"Error_message": "Failed on Authorization"}), status=200, mimetype="application/json")
    #if counter > 250:
    #    return Response(response={"Error_message": "Your subscription has been over (0 runs on the balance)."},
    #                    status=200, mimetype="application/json")

    f = open("counter.txt", "w")
    f.write(counters.replace("-W485M530G1445F1226A2026:" + str(counter), "-W485M530G1445F1226A2026:" + str(counter + 1)))
    f.close()

    nline = False
    try:
        f = open("Request_History/-W485M530G1445F1226A2026.txt", "r")
        txt = f.read()
        f.close()

        nline = True
    except:
        f = open("Request_History/-W485M530G1445F1226A2026.txt", "w")
        f.close()
        txt = ""



    file = request.files['front']
    img = Image.open(file.stream)
    img.save(f"uploads/front-{rand_front}.png")
    read = read_passport(f"uploads/front-{rand_front}.png")


    # file_back = request.files['back']
    # img_back = Image.open(file_back.stream)
    # img_back.save(f"uploads/back-{rand_front}.png")
    # read_back = read_pass_back(f"uploads/back-{rand_front}.png")


    response = {'Front': read}
    #, 'Back':read_back
    if nline:
        txt += "\n"
    txt += "img_id: front-" + str(rand_front) + ".png  count: " + str(counter) + "  time: " + str(datetime.now())
    f = open("Request_History/-W485M530G1445F1226A2026.txt", "w")
    f.write(txt)
    f.close()
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")

@app.route('/I26T290B2810-S257Z325P626M577Q842Q1226X1', methods=['POST'])
def test3():
    rand = random.randint(1, 100000)
    f = open("counter.txt", "r")
    counters = f.read()
    f.close()
    counter = "NONE"
    countering = counters.split("\n")
    for i in countering:
        if "I26T290B2810-S257Z325P626M577Q842Q1226X1" in i:
            counter = int(i.split(":")[1])

    if counter == "NONE":
        return Response(response=jsonpickle.encode({"Error_message": "Failed on Authorization"}), status=200, mimetype="application/json")
    if counter > 100:
        return Response(response=jsonpickle.encode({"Error_message": "Your subscription has been over (0 runs on the balance)."}),
                        status=200, mimetype="application/json")

    f = open("counter.txt", "w")
    f.write(counters.replace("I26T290B2810-S257Z325P626M577Q842Q1226X1:" + str(counter), "I26T290B2810-S257Z325P626M577Q842Q1226X1:" + str(counter + 1)))
    f.close()

    nline = False
    try:
        f = open("Request_History/I26T290B2810-S257Z325P626M577Q842Q1226X1.txt", "r")
        txt = f.read()
        f.close()

        nline = True
    except:
        f = open("Request_History/I26T290B2810-S257Z325P626M577Q842Q1226X1.txt", "w")
        f.close()
        txt = ""

    r = request
    try:
        nparray = np.fromstring(r.data, np.uint8)
        img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)
    except:

        return Response(response=jsonpickle.encode({"Error_message": "Couldn't get your Image"}), status=200, mimetype="application/json")

    cv2.imwrite(f"uploads/{rand}.png", img)

    try:
        read = read_passport(f"uploads/{rand}.png")
    except:
        return Response(response=jsonpickle.encode({"Error_message": "Couldn't process your image"}), status=200,
                        mimetype="application/json")

    response = {'Front': read}
    if nline:
        txt += "\n"
    txt += "img_id: " + str(rand) + ".png  count: " + str(counter) + "  time: " + str(datetime.now())
    f = open("Request_History/I26T290B2810-S257Z325P626M577Q842Q1226X1.txt", "w")
    f.write(txt)
    f.close()
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")



@app.route("/code/<string:code_encoder>")
def encoder(code_encoder):
    dec = zypl_decoder(code_encoder)
    return dec


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def run(server_class=HTTPServer, handler_class=Handler):
    server_address = ('176.57.208.148', 2354)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    app.run(host='176.57.208.148', port=2354)
    run()
