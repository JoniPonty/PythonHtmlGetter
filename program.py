import re
import requests

r = requests.get("https://de.wikipedia.org/wiki/Mittelalter")
r = r.text
r = re.split('href="|"', r)
count = 0
i = 0
for x in r:
    if re.match("^http[s]?:", x):
        count += 1
f = open("output.txt" ,"w")
for x in r:
    if re.match("^http[s]?:", x):
        i+=1
        if "\\" in x:
            x = x.replace("\\", "")
        print(str(i) + " / " + str(count) + "    " + x)
        try:
            ra = requests.get(x)
            if ra.status_code == 200:
                f.write(ra.text)
        except:
            print("THREW AN ERROR")
f.close()
