"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

def defangIPaddr(self, address):
    org = []

    for i in address:
        if i == ".":
            org.append("[.]")
        else:
            org.append(i)
            
    return ''.join(org)

print(defangIPaddr(0,"1.1.1.1"))