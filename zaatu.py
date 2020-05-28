import bisect
def zaatu(a):
    b=sorted(a)
    for i in range(len(a)):
        a[i]=bisect.bisect_left(b,a[i])
    return a