def Csum(a):
    b,c=[0],0
    for i in range(len(a)):
        c+=a[i]
        b.append(c)
    return b
