# Check if the ip address is available
# Created on Dec 31st,2019 by Tony Zhang

# Import necessary modules
import http.client
import socket

# Define a function to check an IP list
ip_list = []
domain = ""
available_ip_list = []

def ip_checking(ip_list, domain, available_ip_list):
    print("\n"+"Check the availability of IP..."+"\n")
    for ip in ip_list:
        check_url = ip+":80"        # Generate a URL according to the ip
        headers = {"Host": domain}
        # Check IP under HTTP protocol
        http_checker = http.client.HTTPConnection(check_url, timeout=5)
        try:
            http_checker.request("GET", "/", headers=headers)
            http_response = http_checker.getresponse()
            if http_response.status == 200: # Current ip is capable of being linked
                available_ip_list.append(ip)
        except socket.timeout as error:
            print(ip, "is an unavailable IP:", error, "\n")
            return
    return available_ip_list
    