def divisors(n):
    d=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            d.append(i)
            if i!=n//i:
                d.append(n//i)
    d.sort()
    return d