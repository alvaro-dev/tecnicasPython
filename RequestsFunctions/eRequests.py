import requests

r = requests.get('http://www.bbc.co.uk')

print(r.text)
print(r.status_code)
