import subprocess
import csv
import time
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
import json
import re
install('pillow')
from PIL import Image
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
la = []
so_many_of_them = 0
la1 = []
list2 = []
garn47 = []
za_count = 0
list3 = []
pi = 0
Tr_cntr = 0
omg = 0
True_count = 0
global abba
count = 0
n_count = 0
county = 3
bruh = 0
coconut = 0
# u = "agawa;aragwa;wawa;bauwa"
def bigger(file, x_size, y_size, use_baw):
    with Image.open(file) as fil:
        fil.load()
    if use_baw == 1:
        thresh = 200
        fn = lambda x : 255 if x > thresh else 0
        fil = fil.convert('L').point(fn, mode='1')
    new = fil.resize((x_size,y_size))
    return(new)
#     if usage == 1:
#         ar = '#bb0000'
#     else:
#         ar = '#000000'
#     dwg = open(file, "w")
#     dwg.write(f"""<?xml version="1.0" encoding="utf-8" ?>
# <svg baseProfile="basic" height="{x_scale}" version="1.1" width="{y_scale}" xmlns="http://www.w3.org/2000/svg"
#     xmlns:ev="http://www.w3.org/2001/xml-events" xmlns:xlink="http://www.w3.org/1999/xlink">
#     <defs />
#     <rect fill="white" height="{x_scale}" stroke="{ar}" width="{y_scale}" x="0" y="0" />
# </svg>""")
#     dwg.close()
#     drawing = svg2rlg(file)
#     renderPM.drawToFile(drawing, "file.png", fmt="PNG")
#     z = open('file.png')
#     return(z)
def Make_It_Readable(x):
    # print(x.replace("""[""", """""").replace("""]""", """""").replace("""'""", """""").replace(""";""", """-"""))
    return(x.replace("""[""", """""").replace("""]""", """""").replace("""'""", """""").replace(""" """, """
""").replace("""'""", """""").replace(""",""", """ """).replace("""
""", """"""))
# # Make_It_Readable(y)
# # Make_It_Readable(u)
# # if False:   
# N = 0
def Make_inf(x):
    x = open(x, encoding='utf-8')
    file_reader = csv.DictReader(x, delimiter = ";")
    return(file_reader)
        # for row in file_reader:
        #     print(f' {row["ID"]} - {row["IP"]} - {row["MAC"]} - {row["SN"]}')
def finnaly_make_it(x, y):
    z = x[y]
# def make_QR(x):
#     img = qrcode.make(x)
#     type(img)
#     img.save("QR.png")
#     with Image.open('QR.png') as QR:
#         QR.load()
#     QR.show()
def make_QR(File, Info, Link, loc_x, loc_y):
    img = qrcode.make(str(Info) + " visit us at: " + Link)
    img.save("QR.png")
    og = File
    with Image.open("QR.png") as QR:
        QR.load()
    og.paste(QR, (loc_x, loc_y))
    return(og)
def make_text(file, What_to_print, font_size, x, y):
    Font = ImageFont.truetype("C:/Users/Reva.A/The_installation/ok.ttf", size=font_size)
    drawText = ImageDraw.Draw(file)
    drawText.text((x,y), Make_It_Readable(str(What_to_print)), fill=('#ae0817'), font=Font, spacing=100)
    file.save("Preset.png")
    x = Image.open("Preset.png")
    return(x)
lo = int(op[0]["Scale_multiplyer"])
po = 1080 * lo
io = 1980 * lo
# bigger("gfx.png", po, io, int(op[0]["Use_company_colors"])).save('another.png')
while True:
    for row in Make_inf("printer.csv"):
        if count < len(op[0]["Objects"]):
            if op[0]['Objects'][count]['Type'] == "text":
                print(f"{row[op[0]['Objects'][count]]}")
            if op[0]['Objects'][count]['Type'] == "text":
                print(f"{row[op[0]['Objects'][count]]}")
        count += 1
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
#         print(list2)
#         for i in range(len(list2)-1):
#             if n_count == 0:
#                 n_count += 1
#             n_count += 2
#             print(list2[n_count])
#             if list2[n_count] == 'text':
#                 list3.append(list2[so_many_of_them])
#                 so_many_of_them +=1
#                 if len(list3) == len(list2) / 2:
#                     p = make_text(bigger(op[0]['destination_preset'], 1980 * int(op[0]['Scale_multiplyer']), 1080 * int(op[0]['Scale_multiplyer']), op[0]['Use_company_colors']), str(list2), 50, 200, 200)
#                     True_count += 1
#             if list2[n_count] == 'QR':
#                 pa = make_QR(bigger(op[0]['destination_preset'], 1980 * int(op[0]['Scale_multiplyer']), 1080 * int(op[0]['Scale_multiplyer']), op[0]['Use_company_colors']), str(list2), op[0]['Link'], 1300, 200)
#                 pa.save(op[0]["dest_output"] + "printer"  + str(True_count) + ".png")
#                 True_count += 1
#             Tr_cntr += 1
#             count = 0
#             if n_count == len(list2)-1:
#                 n_count = 0
#             if p != 0:
#                 p.save(op[0]["dest_output"] + "printer"  + str(True_count) + ".png")
#         za_count = 0
#         list2 = []
#     count += 1