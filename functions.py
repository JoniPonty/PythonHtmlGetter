import re

def getName(_text):
    r = re.findall("<title>.*<\/title>", _text)
    r = r[0]
    r = r.replace("<title>", "")
    r = r.replace("</title>", "")
    return r

def getFile(_link):
    r = _link.split("/")
    r = r[-1]
    return r
