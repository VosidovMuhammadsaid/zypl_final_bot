'''
take image
find and crop passport from the image
crop text fields from the image we get
read all data with PaddleOCR
post processing
return one dict with all variables
DONE!
'''


def convert_to_russian(text):
    new_text = ""
    text += " "
    text = text.upper()
    to_read = False
    for i in range(len(text)):
        if not to_read:
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
                        if text[i + 2] == " ":
                            return new_text
                        to_read = True
                        continue
                    if text[i + 1] == "K":
                        new_text += "К"
                        if text[i + 2] == " ":
                            return new_text
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
                        if text[i + 2] == " ":
                            return new_text
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
                        if text[i + 2] == " ":
                            return new_text
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
                        if text[i + 2] == " ":
                            return new_text
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
                        if text[i + 2] == " ":
                            return new_text
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
                        if text[i + 2] == " ":
                            return new_text

                        to_read = True
                        continue
                except:
                    pass
                new_text += "З"
                continue
        else:
            to_read = False

    return new_text



def clear_text(text, excepts):
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
        i = i.replace("]", "")
        i = i.replace("/", "")
        i = i.replace("?", "")
        i = i.replace("©", "")
        if excepts!=" ":
            i = i.replace(" ", "")
        i = i.replace("|", "")
        i = i.replace(".", "")
        i = i.replace(",", "")
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





from paddleocr import PaddleOCR
from PIL import Image
import numpy as np
import numpy
import cv2

ocr = PaddleOCR(use_angle_cls=True, lang='en')


def bubble_sort(our_list, list2):
    for i in range(len(our_list)):
        for j in range(len(our_list) - 1):
            if our_list[j] > our_list[j + 1]:
                our_list[j], our_list[j + 1] = our_list[j + 1], our_list[j]
                list2[j], list2[j + 1] = list2[j + 1], list2[j]
    return our_list, list2


def sort_indices(text):
    l_index = []
    l_xs = []
    for i in range(0, int(len(text) / 5)):
        l_index.append(text[i * 5])
        l_xs.append(text[i * 5 + 1])
    l_xs, l_index = bubble_sort(l_xs, l_index)
    return l_index


def easy(all_rrr):
    indices = ['1', '0', '2', '3', '4', '5', '6', '7', '8', '9']
    mass = []
    for it in all_rrr:
        text = ""
        for i in range(1, len(it)):
            text += it[i]
            text += "\n"
        word = []
        text = text.replace("\n", " ")
        text = text.split()
        w_indices = sort_indices(text)
        for i in range(len(w_indices)):
            word.append(indices[int(w_indices[i])])
            word[i] = word[i].lower()
        mas = [it[0], "".join(word)]
        mass.append(mas)
    return mass


def alish(ind, str, text):
    d = []
    for i in text:
        d.append(i)
    d.insert(ind, str)
    d.pop(ind + 1)
    s = ''.join(d)
    return s


def alish_be(ind, str, text):
    d = []
    for i in text:
        d.append(i)
    d.insert(ind, str)
    s = ''.join(d)
    return s


def tochka(date):
    if not(date[0]=="A") and len(date) == 8:
        date.replace(".","")
        date = date[0] + date[1] + "." + date[2] + date[3] + "." + date[4] + date[5] + date[6] + date[7]
    return date


def aaa(front):
    for i in range(len(front)):
        if front[0] == "4":
            front = alish(0, "A", front)
        if front[0] == "0" and len(front) == 8:
            front = alish_be(0, "A", front)
    return front


def mask_blur(img):
    try:
        img = cv2.imread(img)
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        im = cv2.filter2D(img, -1, kernel)
        blurred = cv2.GaussianBlur(im, (3, 3), 0)
        kernel2 = np.ones((3, 2), np.uint8)
        e = cv2.erode(blurred, kernel2)
        cv2.imwrite(f'blur.jpg', e)
    except:
        pass


def mask_grainy(img):
    try:
        img = cv2.imread(img)
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        im = cv2.filter2D(blurred, -1, kernel)
        hsv = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
        greenMask = cv2.inRange(hsv, (10, 10, 10), (60, 150, 150))
        im[greenMask == 255] = (50, 60, 60)
        kernel2 = np.ones((3, 2), np.uint8)
        e = cv2.erode(im, kernel2)
        cv2.imwrite(f'grainy.jpg', e)
    except:
        pass


def crop_pass_front(img):
    imgQ = cv2.imread('front_train.jpg', 0)
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


def crop_fields(img):
    Surname_en = img[145:186, 270:550]
    Name_en = img[216:250, 270:550]
    Fathers_Name_en = img[284:316, 270:550]
    Date_of_Birth = img[342:371, 440:570]
    Date_of_Issue = img[392:422, 270:400]
    Date_of_Expiry = img[392:422, 440:570]
    Pass_Number = img[453:550, 10:250]
    return [Surname_en, Name_en, Fathers_Name_en, Date_of_Birth, Date_of_Issue, Date_of_Expiry, Pass_Number]



def read_paddle(fields):
    texts = []
    c=1
    for img in fields:
        text = ocr.ocr(img)
        try:
            texts.append(text[0][0][1][0])
        except:
            texts.append('Empty')
        c+=1
    return texts


def return_dict(letters):
    letters.insert(0, convert_to_russian(letters[0]))
    letters.insert(2, convert_to_russian(letters[2]))
    letters.insert(4, convert_to_russian(letters[4]))

    all_values = {'Surname_rus': '', 'Surname_eng': '', 'Name_rus': '', 'Name_eng': '', 'Fathers_Name_rus': '', 'Fathers_Name_eng': '', 'Date_of_Birth': '', 'Date_of_Issue': '', 'Date_of_Expiry': '', 'Pass_Number': ''}
    letter = ['Surname_rus', 'Surname_eng', 'Name_rus', 'Name_eng', 'Fathers_Name_rus', 'Fathers_Name_eng', 'Date_of_Birth', 'Date_of_Issue', 'Date_of_Expiry', 'Pass_Number']
    ans = ''
    for let in range(len(letters)):
        if letter[let] in ['Date_of_Birth', 'Date_of_Issue', 'Date_of_Expiry', 'Pass_Number']:

            all_values[letter[let]] = tochka(letters[let])
            ans += letter[let] + ' - ' + tochka(letters[let]) + '\n'
        else:
            all_values[letter[let]] = letters[let]
            ans += letter[let] + ' - ' + letters[let] + '\n'
    return all_values


def read_passport(img):
    cropped_img = crop_pass_front(img)
    fields = crop_fields(cropped_img)
    general = read_paddle(fields)
    return return_dict(general)


'''
Docs:
Input: Path of your Passport file
Output: All information in passport(in dictionary or string)
Example: read_passport(path/of/your/file)
'''