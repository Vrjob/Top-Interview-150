def findPerfectNumbers1(n):
    perfectList = []
    i = 1

    while i < n:
        sum = 0
        for j in range(1,i):
            if(i % j == 0):
                sum += j  
        if (sum == i):
            perfectList.append(i)

        i += 1
    print(perfectList)

def primeFactorsSum(num):
    result = 1
    p = 2

    while p * p <= num:
        if num % p == 0:
            j = p * p
            num //= p
            while num % p == 0:
                j *= p
                num //= p
            result *= (j - 1)
            result //= (p - 1)
        if p == 2:
            p = 3
        else:
            p += 2
    if num > 1:
        result *= (num + 1)
    return result

def findPerfectNumbers2(n):
    perfectList = []
    for i in range(2, n):
        if primeFactorsSum(i) == 2 * i:
            perfectList.append(i)
    return perfectList



