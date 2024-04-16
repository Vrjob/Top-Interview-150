"""
You own a Goal Parser that can interpret a string command. 
The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", 
and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.
"""
def interpret1(self, command):
    new = command.replace("(al)","al")
    new = new.replace("()","o")
    return new

def interpret2(self, command):
    return command.replace("(al)","al").replace("()","o")
