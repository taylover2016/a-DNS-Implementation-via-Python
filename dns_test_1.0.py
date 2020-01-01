from dns import resolver

ans = resolver.query("apple.com", "A")
print("qname:", ans.qname)
print("reclass:", ans.rdclass)
print("rdtype:", ans.rdtype)
print("rrset:", ans.rrset)
print("response:", ans.response)
