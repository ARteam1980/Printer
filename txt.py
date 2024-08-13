 #! Библиотеки
import barcode
from barcode.writer import ImageWriter
from collections import defaultdict
import csv
import subprocess
import time
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("tk")
import tkinter as tk
import json
import re
ta = []
install('pillow')
from PIL import Image
from PIL import ImageTk
from PIL import ImageFont
from PIL import ImageDraw
install('numpy')
import numpy as np
install('pandas')
import pandas as pd
install('qrcode')
import qrcode
from io import StringIO
with open('cfg.json') as a:
    op = json.load(a)
list5 = []
list6 = []
list7 = []
list8 = []
p = 0
pa = 0
to = 0
ta = 0
ratatata = 0
la = []
so_many_of_them = 0
la1 = []
more = 0
list2 = []
garn47 = []
za_count = 0
list3 = []
list4 = []
dara = 0
Tr_cntr = 0
omg = 0
omg1 = 0
True_count = 0
global abba
count = 0
n_count = 0
county = 3
bruh = 0
coconut = 0
#? Создание изображения с определённым размером и использованием чб
def Make_Bar(file, what_to_print, protocol, loc_x, loc_y):
    EAN = barcode.get_barcode_class(protocol)
    my_ean = EAN(str(what_to_print), writer=ImageWriter())
    my_ean.save("bar")
    p = Image.open("bar.png")
    zb = file
    zb.paste(p, (loc_x, loc_y))
    return(zb)
def bigger(file, x_size, y_size, use_baw):
    with Image.open(file) as fil:
        fil.load()
    if use_baw == 1:
        thresh = 200
        fn = lambda x : 255 if x > thresh else 0
        fil = fil.convert('L').point(fn, mode='1')
    new = fil.resize((x_size,y_size))
    return(new)
#* Создаёт словарь из csv файла
def Make_inf(x):
    y = open(x, encoding='utf-8')
    file_reader = csv.DictReader(y, delimiter = ";")
    return(file_reader)
#* Создаёт QR код из исходного изображения
def make_QR(File, Info, Link, loc_x, loc_y):
    img = qrcode.make(str(Info) + " visit us at: " + Link)
    img.save("QR.png")
    with Image.open("QR.png") as QR:
        QR.load()
    File.paste(QR, (loc_x, loc_y))
    return(File)
#* Добавляет текст на изображение
def make_text(file, What_to_print, font_size, x, y, font_loc):
    Font = ImageFont.truetype(font_loc, size=font_size)
    drawText = ImageDraw.Draw(file)
    drawText.text((x,y), What_to_print, fill=('#ae0817'), font=Font, spacing=100)
    return(file)
lo = int(op[0]["Scale_multiplyer"])
po = 1980 * lo
io = 1080 * lo
abba = bigger(op[0]["destination_preset"], po, io, int(op[0]["Use_company_colors"]))
columns = defaultdict(list)
pla = Make_inf("Printer.csv")
lern = int(input("Do you want to debug?: "))
while True:
    #! The part that needs editing. We need to create the cycle that comepletly disolves the need of creating combined functions.
    for row in Make_inf("printer.csv"):
        if count >= len(op[0]['Objects']):
            count = 0
        if op[0]['Objects'][count]['Type'] == "text":
            list2.append(row[op[0]["Objects"][count]["Name"]])
        if op[0]['Objects'][count]['Type'] == "QR":
            list3.append(row[op[0]["Objects"][count]["Name"]])
        if op[0]['Objects'][count]['Type'] == "Bar":
            list4.append(row[op[0]["Objects"][count]["Name"]])
        if op[0]['Objects'][count]['Type'] == "text_QR":
            list5.append(row[op[0]["Objects"][count]["Name"]])
        if op[0]['Objects'][count]['Type'] == "text_Bar":
            list6.append(row[op[0]["Objects"][count]["Name"]])
        if op[0]['Objects'][count]['Type'] == "QR_Bar":
            list7.append(row[op[0]["Objects"][count]["Name"]])
        if op[0]['Objects'][count]['Type'] == "text_QR_Bar":
            list8.append(row[op[0]["Objects"][count]["Name"]])
        if count == len(op[0]['Objects']) - 1: 
            if list2 != []:
                make_text(abba,str(list2).replace("""'""", "").replace("""[""", "").replace("""]""", "").replace(""" """, """
""").replace(""",""", ""), op[0]["Objects"][count]["Font_Size"], op[0]["Objects"][count]["loc_x"], op[0]["Objects"][count]["loc_y"], op[0]["font_loc"]).save(op[0]["dest_output"] + f"printer{ratatata}.png")
                list2 = []
            if list3 != []:
                make_QR(abba, str(list3), op[0]["Link"], op[0]["Objects"][count]["loc_x"], op[0]["Objects"][count]["loc_y"]).save(op[0]["dest_output"] + f"printer{ratatata}.png")
                list3 = []
            if list4 != []:
                Make_Bar(abba, str(list4).replace("""'""", "").replace("""[""", "").replace("""]""", ""), op[0]["Protocol"], op[0]["Objects"][count]["loc_x"], op[0]["Objects"][count]["loc_y"]).save(op[0]["dest_output"] + f"printer{ratatata}.png")
                list4 = []
            if list5 != []:
                make_QR(make_text(abba,str(list5).replace("""'""", "").replace("""[""", "").replace("""]""", "").replace(""" """, """
""").replace(""",""", ""), op[0]["Objects"][count]["Font_Size"], op[0]["Objects"][count]["loc_x"], op[0]["Objects"][count]["loc_y"], op[0]["font_loc"]), str(list5).replace("""'""", "").replace("""[""", "").replace("""]""", "").replace(""",""", ""), op[0]["Link"], op[0]["Objects"][ratatata]["loc_x"], op[0]["Objects"][ratatata]["loc_y"])
                list5 = []
            if list6 != []:
                Make_Bar(make_text(abba,str(list6).replace("""'""", "").replace("""[""", "").replace("""]""", "").replace(""" """, """
""").replace(""",""", ""), op[0]["Objects"][count]["Font_Size"], op[0]["Objects"][count]["loc_x"], op[0]["Objects"][count]["loc_y"], op[0]["font_loc"]), str(list6).replace("""'""", "").replace("""[""", "").replace("""]""", "").replace(""",""", ""), op[0]["Protocol"], 1200, 200)
                list6 = []
            if list7 != []:
                Make_Bar(make_QR(abba,str(list7).replace("""'""", "").replace("""[""", "").replace("""]""", "").replace(""" """, """
""").replace(""",""", ""), op[0]["Link"], op[0]["Objects"][count]["loc_x"], op[0]["Objects"][count]["loc_y"]), str(list7).replace("""'""", "").replace("""[""", "").replace("""]""", "").replace(""",""", ""), op[0]["Protocol"], 1200, 200)
                list7 = []
            if list8 != []:
                Make_Bar(make_QR(abba,str(list7).replace("""'""", "").replace("""[""", "").replace("""]""", "").replace(""" """, """
""").replace(""",""", ""), op[0]["Link"], op[0]["Objects"][count]["loc_x"], op[0]["Objects"][count]["loc_y"]), str(list7).replace("""'""", "").replace("""[""", "").replace("""]""", "").replace(""",""", ""), op[0]["Protocol"], 1200, 200)
                list8 = []
            ratatata += 1
        if count >= len(op[0]['Objects']):
            count = 0
            
        print(f"{op[0]['Objects'][count]["Type"]}")
        to = 0
        ta = 0
        count += 1
        more += 0
# while count != round(len(Make_inf(str(op[0]['destination_csv']))) / len(op[0]['Objects']) - 1):
#     y = len(list(op[0]['Objects'])) * count
#     za = Make_It_Readable(str(Make_inf(op[0]['destination_csv'])[county]))
#     if za_count != len(list(op[0]['Objects'])):
#         county += 1
#         if op[0]['Objects'][za_count]['Type'] == 'text':
#             list2.append(za)
#             list2.append('text')
#         if op[0]['Objects'][za_count]['Type'] == 'QR':
#             list2.append(za)
#             list2.append('QR')
#         if op[0]['Objects'][za_count]['Type'] == 'DATA':
#             list2.append(za)
#             list2.append('DATA')
#         za_count += 1
#     else:
#         for i in range(len(list2)-1):
#             if n_count == 0:
#                 n_count += 1
#             n_count += 2
#             if list2[n_count] == 'text':
#                 print(list4)
#                 list3.append(list2[omg])
#                 if len(list3) == len(list2) / 2:
#                     p = make_text(bigger(op[0]['destination_preset'], 1980 * int(op[0]['Scale_multiplyer']), 1080 * int(op[0]['Scale_multiplyer']), op[0]['Use_company_colors']), str(list3), 50, 200, 200)
#                     list3 = []
#             if list2[n_count] == 'QR':
#                 list4.append(list2[omg])
#                 if len(list4) == len(list2) / 2:
#                     print(list4)
#                     if p == 0:
#                         pa = make_QR(bigger(op[0]['destination_preset'], 1980 * int(op[0]['Scale_multiplyer']), 1080 * int(op[0]['Scale_multiplyer']), op[0]['Use_company_colors']), str(list4), op[0]['Link'], 1300, 200)
#                     else:
#                         pa = make_QR(p, str(list4), op[0]['Link'], 1300, 200)
#                     True_count += 1
#                     list4 = []
#             Tr_cntr += 1
#             aaaa += 1
#             count = 0
#             if n_count == len(list2)-1:
#                 n_count = 0
#             if o == 1:
#                 if p != 0 and pa == 0:
#                     p.save(op[0]["dest_output"] + "printer"  + str(True_count) + ".png")
#                     p = 0
#                     True_count += 1
#                 if pa != 0 and p == 0:
#                     pa.save(op[0]["dest_output"] + "printer"  + str(True_count) + ".png")
#                     pa = 0
#                     True_count += 1
#                 if p != 0 and pa != 0:
#                     pa.save(op[0]["dest_output"] + "printer"  + str(True_count) + ".png")
#                     p = 0
#                     pa = 0
#                     True_count += 1
#             omg += 2
#             if aaaa >= len(list2) - 2:
#                 aaaa = 0
#             if omg == len(list2):
#                 omg = 0
#         za_count = 0
#         list2 = []
#     count += 1
