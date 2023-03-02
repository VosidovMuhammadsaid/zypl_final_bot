import random
import numpy as np

def zypl_encoder(in_text, secret=1):
    out_text = ""
    temp_text = ""
    for i in range(len(in_text)):
        temp_text = ""
        r_num = random.randint(65, 90)
        letter = chr(r_num)
        dif = ord(in_text[i]) - r_num
        if dif < 0:
            temp_text += "-"
            dif = -1 * dif
        temp_text += letter
        temp_text += str((dif * dif) + secret)
        temp_text += ""
        out_text += temp_text
    return out_text


def zypl_decoder(in_text, secret=1):
    out_text = ""
    letters = []
    temp_text = ""
    texts = []
    is_negative = False
    in_text += 'A'
    if in_text[0] == "-":
        is_negative = True
    for i in range(len(in_text)):

        if i == 0 and is_negative:
            continue
        if in_text[i].isalpha():

            texts.append(temp_text)
            if i > 1:
                temp_text = ""
        temp_text += in_text[i]

    for i in range(len(texts)):
        letters.append("")

    if is_negative:
        letters[1] += "-"
    for i in range(len(texts)):
        if "-" in texts[i]:
            letters[i + 1] += "-"
        letters[i] += texts[i].replace("-", "")
    letters.pop(0)

    decrypted = []
    for i in range(len(letters)):
        is_negative = False
        temp_text = ""
        if letters[i][0] == "-":
            is_negative = True
            letters[i] = letters[i].replace("-", "")
        character = letters[i][0]

        letters[i] = letters[i].replace(character, "")

        character = ord(character)

        ans = np.sqrt(int(letters[i]) - secret)

        if is_negative:
            ans = -1 * ans

        decrypted.append(chr(int(ans) + int(character)))

    ans = ""
    for i in decrypted:
        ans += i
    return ans

# -W485M530G1445F1226A2026
# -S101D1682Z442N1025
# I26T290B2810-S257Z325P626M577Q842Q1226X1