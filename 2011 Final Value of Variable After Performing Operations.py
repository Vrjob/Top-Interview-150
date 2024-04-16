"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, 
return the final value of X after performing all the operations.
"""

def finalValueAfterOperations(self, operations):
    org = []

    for op in operations:
        if op == "++X" or op == "X++":
            org.append(1)
        if op == "--X" or op == "X--":
            org.append(-1)
    
            
    return sum(org)

def finalValueAfterOperations2(self, operations):
    org = []

    for i in range(len(operations)):
        if operations[i] == "++X" or operations[i] == "X++":
            org.append(1)
        elif operations[i] == "--X" or operations[i] == "X--":
            org.append(-1)
        
    return sum(org)

def finalValueAfterOperations3(self, operations):
    count = 0
    for i in operations:
        if i == "X--" or i == "--X":
            count -= 1
        else:
            count += 1
    return (count)

print(finalValueAfterOperations2(0,["--X","X++","X++"]))