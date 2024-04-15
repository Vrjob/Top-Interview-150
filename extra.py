def reverseArray(a):
    b = []
    valido = True
    
    if 1<= len(a) and len(a) <= 10**3:
        for i in a:
            if i < 1:
                valido = False
            elif i > 10**4:
                valido = False
            
        if valido:
            for i in range(len(a)):
                b.append(a[len(a)-1-i]) 

            return b
        

print(reverseArray([4,3,2,1,888]))

