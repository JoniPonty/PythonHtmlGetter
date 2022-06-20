import re
import sys
import requests
import os
from functions import *

arg_link = str(sys.argv[1])
link_array = requests.get(arg_link)
link_array = link_array.text
link_array = re.split('href="|"', link_array)
count = 1
amount = 0
for link in link_array:
    if re.match("^http[s]?://.", link):
        count += 1
output_index = open("./output/index.html", "w")
data_index = open("./data/index.html", "w")
output_index.write('<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>index</title></head><body>')
data_index.write('<!DOCTYPE html><html lang="en"><head>    <meta charset="UTF-8">    <title>index</title></head><body>')
link_array.append(sys.argv[1])
for link in link_array:
    if re.match("^http[s]?://.", link):
        amount+=1
        if "\\" in link:
            link = link.replace("\\", "")
        print(str(amount) + " / " + str(count) + "    " + link)
        try:
            request = requests.get(link)
            if request.status_code == 200:
                try:
                    name = getName(request.text)
                    file_output = open("./output/" + name, "w")
                    output_index.write('<a href="' + name + '"><p>' + name + '</p></a>')
                    output_index.write("\n")
                    file_output.write(request.text)
                    file_output.close()
                except:
                    name = getFile(link)
                    file_data = open("./data/" + name, "w")
                    data_index.write('<a href="' + name + '"><p>' + name + '</p></a>')
                    data_index.write("\n")
                    file_data.write(request.text)
                    file_data.close()
        except:
            print("THREW AN ERROR")

output_index.write('</body></html>')
data_index.write('</body></html>')
output_index.close()
data_index.close()
os.system("sudo bash move.sh")
