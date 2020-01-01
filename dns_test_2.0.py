import dns.resolver
import http.client
import urllib.parse

domain = "www.bfsu.edu.cn"

ip_list = []

a_query = dns.resolver.query(domain, 'A')

for i in a_query.response.answer:
    for j in i.items:
        if j.rdtype == 1:
            ip_list.append(j.address)

print("The available IP are listed below:")
for i in ip_list:
    print(i)

for ip in ip_list:
    check_url = ip+":80"
    headers = {"Host": domain}
    http_request = http.client.HTTPConnection(check_url, timeout=5)
    http_request.request("GET", "/", headers=headers)
    response = http_request.getresponse()
    print(response.status)
    print(response.reason)
