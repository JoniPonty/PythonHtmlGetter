import re
import requests
import os

r = requests.get("https://ctemplar.com")
r = r.text
r = re.split('href="|"', r)
count = 0
i = 0
for x in r:
    if re.match("^http[s]?:", x):
        count += 1
a = open("./output/index.html", "w")
a.write('<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>index</title></head><body>')
for x in r:
    if re.match("^http[s]?:", x):
        i+=1
        if "\\" in x:
            x = x.replace("\\", "")
        print(str(i) + " / " + str(count) + "    " + x)
        try:
            ra = requests.get(x)
            if ra.status_code == 200:
                f = open("./output/" + str(i) + "output.html", "w")
                a.write('<a href="' + str(i) + 'output.html"><p>'+ str(i) + 'output.html </p></a>')
                a.write("\n")
                f.write(ra.text)
                f.close()
        except:
            print("THREW AN ERROR")
a.write('</body></html>')
a.close()
os.system("sudo bash move.sh")
