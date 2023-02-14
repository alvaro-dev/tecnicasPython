import sys
import requests
import os

url = sys.argv[1]
lista = ["admin","login","css","sport","mail","panel"]
resultURL = ""

os.system("clear")
for i in lista:
    resultURL = "Testando URL ===>" + url + i
    print(resultURL)
    r = requests.get(url + i)
    resultURL = "<== " + str(r.status_code)
    if r.status_code== 200:
        print(resultURL + " ==> ok")
    else:
        print(resultURL + " ==> not found")
        continue