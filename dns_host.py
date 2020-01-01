# A simple DNS protocol implementation
# Created on Jan 1st,2020 by Tony Zhang

# Import necessary modules
import dns.resolver
import ip_checking

# Select the type of name input
query_type = input("\n"+"Please select the type of query:")


# Some lists to store the results
ip_list = []
available_ip_list = []
authority_dns_server = []
mail_server = []
standard_hostname = []


# Define the functions for different type of queries
def a():
    hostname = input("\n"+"Please input a hostname:")
    print("\n"+"Hostname detected, query initiated..."+"\n")
    try:
        A_query = dns.resolver.query(hostname, 'A')
        # Query complete
        print("Query Name:", hostname)
        print("Record Data Type:", A_query.rdtype)
        print("Resource Record Set:", A_query.rrset)
        print("Response:", A_query.response)
        # Save all the IP from RR set
        for i in A_query.response.answer:
            for j in i.items:
                if j.rdtype == 1:
                    ip_list.append(j.address)
        # Check the availability of the IP in the ip_list
        ip_checking.ip_checking(ip_list, hostname, available_ip_list)
        # Return all the available IP
        print("Available IP:")
        for ip in available_ip_list:
            print(ip)
    except dns.resolver.NoAnswer as NoAnswer:
        print(NoAnswer)


def aaaa():
    hostname = input("\n"+"Please input a hostname:")
    print("\n"+"Hostname detected, query initiated..."+"\n")
    try:
        AAAA_query = dns.resolver.query(hostname, 'AAAA')
        # Query complete
        print("Query Name:", hostname)
        print("Record Data Type:", AAAA_query.rdtype)
        print("Resource Record Set:", AAAA_query.rrset)
        print("Response:", AAAA_query.response)
        # Save all the IP from RR set
        for i in AAAA_query.response.answer:
            for j in i.items:
                if j.rdtype == 28:
                    ip_list.append(j.address)
        # Check the availability of the IP in the ip_list
        ip_checking.ip_checking(ip_list, hostname, available_ip_list)
        # Return all the available IP
        print("Available IP:")
        for ip in available_ip_list:
            print(ip)
    except dns.resolver.NoAnswer as NoAnswer:
        print(NoAnswer)


def a6():
    hostname = input("\n"+"Please input a hostname:")
    print("\n"+"Hostname detected, query initiated..."+"\n")
    try:
        A6_query = dns.resolver.query(hostname, 'A6')
        # Query complete
        print("Query Name:", hostname)
        print("Record Data Type:", A6_query.rdtype)
        print("Resource Record Set:", A6_query.rrset)
        print("Response:", A6_query.response)
        # Save all the IP from RR set
        for i in A6_query.response.answer:
            for j in i.items:
                if j.rdtype == 38:
                    ip_list.append(j.address)
        # Check the availability of the IP in the ip_list
        ip_checking.ip_checking(ip_list, hostname, available_ip_list)
        # Return all the available IP
        print("Available IP:")
        for ip in available_ip_list:
            print(ip)
    except dns.resolver.NoAnswer as NoAnswer:
        print(NoAnswer)


def ns():
    domain = input("\n"+"Please input a domain:")
    print("\n"+"Domain detected, query initiated..."+"\n")
    try:
        NS_query = dns.resolver.query(domain, 'NS')
        # Query complete
        print("Query Name:", domain)
        print("Record Data Type:", NS_query.rdtype)
        print("Resource Record Set:", NS_query.rrset)
        print("Response:", NS_query.response)
        # Save all the authority DNS servers to a list
        for i in NS_query.response.answer:
            for j in i.items:
                if j.rdtype == 2:
                    authority_dns_server.append(j.to_text())
        # Output the result
        print("\n" + "Authority DNS Servers:")
        for domain in authority_dns_server:
            print(domain)
    except dns.resolver.NoAnswer as NoAnswer:
        print(NoAnswer)


def mx():
    alias = input("\n"+"Please input an alias:")
    print("\n"+"Alias detected, query initiated..."+"\n")
    try:
        MX_query = dns.resolver.query(alias, 'MX')
        # Query complete
        print("Query Name:", alias)
        print("Record Data Type:", MX_query.rdtype)
        print("Resource Record Set:", MX_query.rrset)
        print("Response:", MX_query.response)
        # Save all the mail servers to a list
        for i in MX_query.response.answer:
            for j in i.items:
                if j.rdtype == 15:
                    mail_server.append(j.exchange)
        # Output the result
        print("\n" + "Hostnames of the mail servers:")
        for hostname in mail_server:
            print(hostname)
    except dns.resolver.NoAnswer as NoAnswer:
        print(NoAnswer)


def cname():
    alias = input("\n" + "Please input an alias:")
    print("\n"+"Alias detected, query initiated..."+"\n")
    try:
        CNAME_query = dns.resolver.query(alias, 'CNAME')
        # Query complete
        print("Query Name:", alias)
        print("Record Data Type:", CNAME_query.rdtype)
        print("Resource Record Set:", CNAME_query.rrset)
        print("Response:", CNAME_query.response)
        # Save all the standard hostname to a list
        for i in CNAME_query.response.answer:
            for j in i.items:
                if j.rdtype == 5:
                    standard_hostname.append(j.to_text())
        # Output the result
        print("\n" + "Standard hostnames:")
        for hostname in standard_hostname:
            print(hostname)
    except dns.resolver.NoAnswer as NoAnswer:
        print(NoAnswer)


def others():
    print("Invalid Input!")


# Use a dictionary to implement the choice of query type
query_type_dict = {"A": a, "AAAA": aaaa, "A6": a6, "NS": ns, "MX": mx, "CNAME": cname}
query_type_dict.get(query_type, others)()
