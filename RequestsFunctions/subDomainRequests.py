import sys
import requests
import os

url = sys.argv[1]
file = open('subs.txt')

os.system("clear")
for line in file:
    line=line.strip()
    sub_to_check = f"https://{line}.{url}"
    try:
        r = requests.get(sub_to_check)
        print( str(r.status_code) + " : " + sub_to_check + " ==> ok")
    except:
        continue