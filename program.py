import re
import requests

r = requests.get("https://en.wikipedia.org/wiki/Text_messaging")
r = r.text
r = re.split('href="|"', r)
for x in r:
    if x.startswith("http"):
        try:
            ra = requests.get(x)
            if ra.status_code == 200:
                print(ra.text)
        except:
            print(x + " THREW AN ERROR")
