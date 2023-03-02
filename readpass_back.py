from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import numpy
import cv2
# import easyocr


ocr = PaddleOCR(use_angle_cls=True, lang='en')
# reader = easyocr.Reader(['tjk'])

def convert_to_russian(text):
    new_text = ""
    text += ""
    text = text.upper()
    to_read = False
    for i in range(len(text)):
        if not to_read:
            if text[i] == " ":
                new_text+=" "
                continue
            if text[i] == "A":
                new_text += "А"
                continue
            if text[i] == "B":
                new_text += "Б"
                continue
            if text[i] == "C":
                try:
                    if text[i + 1] == "H":

                        new_text += "Ч"
                        to_read = True
                        continue
                    if text[i + 1] == "K":
                        new_text += "К"
                        to_read = True
                        continue
                except:
                    pass
                new_text += "К"
                continue
            if text[i] == "D":
                new_text += "Д"
                continue
            if text[i] == "E":
                if i == 0:
                    new_text += "Э"
                    continue
                new_text += "Е"
                continue
            if text[i] == "F":
                new_text += "Ф"
                continue
            if text[i] == "G":
                try:
                    if text[i + 1] == "H":

                        new_text += "Ғ"
                        to_read = True
                        continue
                except:
                    pass
                new_text += "Г"
                continue
            if text[i] == "H":
                new_text += "Ҳ"
                continue
            if text[i] == "I":
                new_text += "И"
            if text[i] == "J":
                new_text += "Ҷ"
            if text[i] == "K":
                try:
                    if text[i + 1] == "H":

                        new_text += "Х"
                        to_read = True
                        continue
                except:
                    pass
                new_text += "К"
            if text[i] == "L":
                new_text += "Л"
                continue
            if text[i] == "M":
                new_text += "М"
                continue
            if text[i] == "N":
                new_text += "Н"
                continue
            if text[i] == "O":
                new_text += "О"
                continue
            if text[i] == "P":
                new_text += "П"
                continue
            if text[i] == "Q":
                new_text += "Қ"
                continue
            if text[i] == "R":
                new_text += "Р"
                continue
            if text[i] == "S":
                try:
                    if text[i + 1] == "H":
                        new_text += "Ш"
                        to_read = True
                        continue
                except:
                    pass
                new_text += "С"
                continue
            if text[i] == "T":
                new_text += "Т"
                continue
            if text[i] == "U":
                new_text += "У"
                continue
            if text[i] == "V":
                new_text += "В"
                continue
            if text[i] == "W":
                new_text += "В"
                continue
            if text[i] == "X":
                new_text += "КС"
                continue
            if text[i] == "Y":
                try:
                    if text[i + 1] == "A":
                        new_text += "Я"
                        to_read = True
                        continue
                    if text[i + 1] == "U":
                        new_text += "Ю"
                        to_read = True
                        continue
                    if text[i + 1] == "O":
                        new_text += "Ё"
                        to_read = True
                        continue
                except:
                    pass
                new_text += "Й"
                continue
            if text[i] == "Z":
                try:
                    if text[i + 1] == "H":

                        new_text += "Ж"
                        to_read = True
                        continue
                except:
                    pass
                new_text += "З"
                continue
        else:
            to_read = False

    return new_text

def clear_text(text):
    d = ""
    for i in text:
        i = i.replace("1", "")
        i = i.replace("2", "")
        i = i.replace("3", "")
        i = i.replace("4", "")
        i = i.replace("5", "")
        i = i.replace("6", "")
        i = i.replace("7", "")
        i = i.replace("8", "")
        i = i.replace("9", "")
        i = i.replace("0", "")
        i = i.replace("'", "")
        i = i.replace(";", "")
        i = i.replace("-", "")
        i = i.replace("!", "")
        i = i.replace("@", "")
        i = i.replace("#", "")
        i = i.replace("%", "")
        i = i.replace("^", "")
        i = i.replace("&", "")
        i = i.replace("(", "")
        i = i.replace(")", "")
        i = i.replace("*", "")
        i = i.replace("_", "")
        i = i.replace("}", "")
        i = i.replace("{", "")
        i = i.replace("[", "")
        i = i.replace("]", " ")
        i = i.replace("/", " ")
        i = i.replace("?", " ")
        i = i.replace("©", " ")
        i = i.replace("|", "")
        i = i.replace("»", "")
        i = i.replace("«", "")
        i = i.replace("\n", "")
        i = i.replace("\t", "")
        i = i.replace("~", "")
        i = i.replace("—", "")
        i = i.replace("”", "")
        i = i.replace("=", "")
        i = i.replace("<", "")
        i = i.replace(">", "")
        i = i.replace('"', "")
        i = i.replace('+', "")
        i = i.replace(':', "")
        i = i.replace("\\", "")
        i = i.replace('\x0c', "")
        i = i.replace('\n', "")
        i = i.replace("`","")
        d += i
    return d


def crop_pass_front(img):
    imgQ = cv2.imread('back_train.jpg', 0)
    h, w = imgQ.shape
    per = 25
    features = 14500
    orb = cv2.ORB_create(features)
    kp1, des1 = orb.detectAndCompute(imgQ, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    im = Image.open(img).convert("RGB")
    open_cv_image = numpy.array(im)
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    img = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    kp2, des2 = orb.detectAndCompute(img, None)
    matches = bf.match(des2, des1)
    matches1 = list(matches)
    matches1.sort(key=lambda x: x.distance)
    good = matches1[:int(len(matches) * (per / 100))]
    imgMatch = cv2.drawMatches(img, kp2, imgQ, kp1, good[:100], None, flags=2)
    srcPoints = numpy.float32([kp2[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dstPoints = numpy.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    M, _ = cv2.findHomography(srcPoints, dstPoints, cv2.RANSAC, 5.0)
    imgScan = cv2.warpPerspective(img, M, (w, h))
    return imgScan


def showlbl(key,img):
    img=cv2.imread(img)
    rt={'marital': [[0.4277511961722488, 0.36882716049382713], [0.5684210526315789, 0.42592592592592593]],
        'issuing_authority': [[0.2535885167464115, 0.5030864197530864], [0.662200956937799, 0.5493827160493827]],
        'tax_payer': [[0.7913875598086124, 0.3734567901234568], [0.9885167464114832, 0.4444444444444444]],
        'address': [[0.2966507177033493, 0.10648148148148148], [0.9339712918660287, 0.25925925925925924]]
    }
    r=rt[key]
    x1,x2=int(img.shape[1]*r[0][0]),int(img.shape[1]*r[1][0])
    y1,y2=int(img.shape[0]*r[0][1]),int(img.shape[0]*r[1][1])
    img=img[y1:y2,x1:x2]
    return img


def marital_status(string):
    ret_text = ""
    if "MARRIED" in string:
        ret_text = "ОИЛАДОР"
    if "SINGLE" in string:
        ret_text = "МУҶАРРАД"

    return ret_text


def issuing_authoraty(string):


    r=string.replace("IN", "")
    r1=r.replace("DISTRICT","")
    r2=r1.replace("CITY","")
    r3=r2.replace("DIA","")
    r4=r3.replace("DMIA","")



    s=""
    if "DMIA" in string or "DIA" in string:
        s+="ШВКД"

    for i in range(1,10):
        if f"-{i}" in string or f"-{i}" in string:
            s+=f"-{i}"

    if "IN" in string:
        s+=" ДАР"

    if "DISTRICT" in string:
        s+=" НОҲИЯИ"
    if "CITY" in string:
        s+=" ШАҲРИ"
    s+=convert_to_russian(clear_text(r4))
    return s

#
# def read_pass_back(img):
#     cv2.imwrite("img/crop.jpg", crop_pass_front(img))
#     cv2.imwrite("img/crop-marital.jpg", showlbl('marital', "img/crop.jpg"))
#     cv2.imwrite("img/crop-issuing_authority.jpg", showlbl('issuing_authority', "img/crop.jpg"))
#     cv2.imwrite("img/crop-tax_payer.jpg", showlbl('tax_payer', "img/crop.jpg"))
#     cv2.imwrite("img/crop-address.jpg", showlbl('address', "img/crop.jpg"))
#
#     labels = ["marital", "issuing_authority", "tax_payer"]
#
#     addr = reader.readtext('img/crop-address.jpg', detail = 0)
#     addr=" ".join(addr)
#
#
#
#     lis = []
#     for i in labels:
#         result = ocr.ocr(f"img/crop-{i}.jpg", det=False, cls=True)[0][0][0]
#         lis.append(result)
#
#     print(lis)
#     final_list=[addr, marital_status(lis[0]), issuing_authoraty(lis[1]), lis[2]]
#
#     dic={
#         "Address": clear_text(final_list[0]),
#         "Marital_status": final_list[1],
#         "Tax_payer_ID_number": final_list[3],
#         "Issuing_Authority": final_list[2]
#     }
#
#     return dic