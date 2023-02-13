import sys
import whois11
import requests

option = sys.argv[1]
target = sys.argv[2]
arg3 = sys.argv[3]

if option==0:
    print(whois11.whois(target))
else:
    r = requests.get(arg3)
    print(r.text)
    print(r.status_code)