import re
import keyboard
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
import re
import numpy as np
import pandas as pd
import qrcode
from io import StringIO
abba = 0
count = 0
# # p = 0
# # x = np.loadtxt(
# #         'text.csv',
# #         usecols= True,
# #         dtype = str,
# #         delimiter = ';',
# #         )
# # y = str(x)
# # u = "agawa;aragwa;wawa;bauwa"
def Make_It_Readable(x):
    # print(x.replace("""[""", """""").replace("""]""", """""").replace("""'""", """""").replace(""";""", """-"""))
    return(x.replace("""[""", """""").replace("""]""", """""").replace("""'""", """""").replace(""" """, """""").replace("""'""", """"""))
# # Make_It_Readable(y)
# # Make_It_Readable(u)



# # if False:
# N = 0
def Make_inf():
    x = np.loadtxt(
        'C:/Users/Reva.A/The_installation/hi/printer.csv',
        dtype = str,
        )
    y = str(x)
    return(re.split(r""";|
""", y))
# def make_QR(x):
#     img = qrcode.make(x)
#     type(img)
#     img.save("QR.png")
#     with Image.open('QR.png') as QR:
#         QR.load()
#     QR.show()
def make_img(L, PG, PeGi, PeGi2, name, baba):
    img = qrcode.make(baba + """
Service site at http://it.loc/search/id=""" + L +"&sn=" + PeGi2 + "@mac=" + PeGi + "@ip=" + PG)
    type(img)
    img.save("QR.png")
    with Image.open('C:/Users/Reva.A/The_installation/examine.png') as img:
        img.load()
    with Image.open('QR.png') as QR:
        QR.thumbnail((3000,3000))
        QR.load()
    img.paste(QR, (1150, 270))
    if int(L) < 100:
        Font = ImageFont.truetype("C:/Users/Reva.A/The_installation/ok.ttf", size=750)
    if int(L) >= 100:
        Font = ImageFont.truetype("C:/Users/Reva.A/The_installation/ok.ttf", size=500)
    Font2 = ImageFont.truetype("C:/Users/Reva.A/Downloads/times.ttf", size=43)
    drawText = ImageDraw.Draw(img)
    if int(L) < 100:
        drawText.text((300,140), L, fill=('#ae0817'), font=Font)
    if int(L) >= 100:
        drawText.text((300,300), L, fill=('#ae0817'), font=Font)
    drawText.text((1190,800), PG, fill=('#ae0817'), font=Font2)
    drawText.text((1400,800), PeGi, fill=('#ae0817'), font=Font2)
    drawText.text((1300,840), PeGi2, fill=('#ae0817'), font=Font2)
    img.save(name)
print(Make_inf())
while count != 60:
    Num = Make_It_Readable(Make_inf()[abba])
    abba+=1
    IP = Make_It_Readable(Make_inf()[abba])
    abba += 1
    MAC = Make_It_Readable(Make_inf()[abba])
    abba += 1
    Ser = Make_It_Readable(Make_inf()[abba])
    abba+=1
    gaga = Num + """
""" + IP + """
""" + MAC + """
""" + Ser
    count+=1
    make_img(Num, IP, MAC, Ser, "C:/Users/Reva.A/The_installation/cards/card" + str(count) + ".png", gaga)    
    

# p = int(input("""Выберите режим использования
# 1. Сгенерировать информацию.
# 2. Сгенерировать Qr код.
# 3. Сделать визитные карточки:  """))
# if(p==1):
#     print(Make_inf)
# if(p==2):
#     make_QR(input())
# while p == 3:
#     make_img()
#     print('Сделать ещё?')
#     N += 43
#     time.sleep(5)
