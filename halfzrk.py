def halfzrk(l):
    a,b=l[::2],l[1::2]
    a1,b1=[],[]
    for i in range(len(a)):
        i=bin(i)[2:].zfill(len(a))
        a1.append(sum([a[j]*int(i[j])for j in range(len(a))]))
    for i in range(len(b)):
        i=bin(i)[2:].zfill(len(b))
        b1.append(sum([b[j]*int(i[j])for j in range(len(b))]))
    return sorted(a1),sorted(b1)