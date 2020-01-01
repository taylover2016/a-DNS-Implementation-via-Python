import requests

domain = "http://220.181.38.148:80"

r = requests.get(domain)

print(r.status_code)