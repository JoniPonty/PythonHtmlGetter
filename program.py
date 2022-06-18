import re
import requests
import os
from functions import *

r = requests.get("https://www.w3schools.com/python/python_try_except.asp")
r = r.text
r = re.split('href="|"', r)
count = 0
i = 0
for x in r:
    if re.match("^http[s]?:", x):
        count += 1
a = open("./output/index.html", "w")
b = open("./data/index.html", "w")
a.write('<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>index</title></head><body>')
b.write('<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>index</title></head><body>')
for x in r:
    if re.match("^http[s]?:", x):
        i+=1
        if "\\" in x:
            x = x.replace("\\", "")
        print(str(i) + " / " + str(count) + "    " + x)
        try:
            ra = requests.get(x)
            if ra.status_code == 200:
                try:
                    name = getName(ra.text)
                    f = open("./output/" + name, "w")
                    a.write('<a href="' + name + '"><p>' + name + '</p></a>')
                    a.write("\n")
                    f.write(ra.text)
                    f.close()
                except:
                    name = getFile(x)
                    o = open("./data/" + name, "w")
                    b.write('<a href="' + name + '"><p>' + name + '</p></a>')
                    b.write("\n")
                    o.write(ra.text)
                    o.close()
        except:
            print("THREW AN ERROR")

a.write('</body></html>')
a.close()
os.system("sudo bash move.sh")
