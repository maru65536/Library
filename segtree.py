import math
inf=10**9
def segtree(a): #RMQ(Range Minimum Query)
    #bi=高さ　bi2=最下段の個数
    global bi 
    bi=(len(a)-1).bit_length()+1
    global bi2
    bi2=2**(bi-1)
    seg=[inf]*(2*bi2-1)
    for i in range(len(a)):
        seg[bi2+i-1]=a[i]
    for i in range(bi-1):
        for j in range(2**(bi-i-2)):
            b=2**(bi-i-2)-1+j
            seg[b]=min(seg[2*b+1],seg[2*b+2])
    return seg

def seg_update(loc,val): #locの値をvalueに更新
    loc+=bi2-1
    seg[loc]=val
    while True:
        seg[loc]=min(val,seg[loc])
        if loc==0:
            break
        loc=(loc-1)//2

def seg_find(l,r,tmp=0): #[l,r)の最小値を求める
    a=bi-math.ceil(math.log2(tmp+2))+1
    nl=2**(a-1)*(tmp-(2**(bi-a))+1)
    nr=nl+2**(a-1)
    if nr<=l or nl>=r:
        return inf
    elif l<=nl and nr<=r:
        return seg[tmp]
    else:
        return min(seg_find(l,r,tmp*2+1),seg_find(l,r,tmp*2+2))

seg=segtree([5,4,3,6,1])
print(seg)
seg_update(1,0)
print(seg)
print(seg_find(0,3))