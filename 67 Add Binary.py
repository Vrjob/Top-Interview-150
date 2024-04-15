"""
Given two binary strings a and b, return their sum as a binary string.

Constraints:
1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
def addBinary(self, a, b):
    if (1 <= len(a) <= 10**4) and (1 <= len(b) <= 10**4):
        if all(bit in '01' for bit in a) and all(bit in '01' for bit in b):
            a = a.lstrip('0') or '0'
            b = b.lstrip('0') or '0'
            res = bin(int(a, 2) + int(b, 2))
            return res[2:]
