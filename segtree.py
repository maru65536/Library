def make_segtree(a): #listからsegtreeを生成して返す
    import math
    #bi=最下段の個数　bi2=高さ
    bi=math.ceil(math.log2(len(a)))+1
    bi2=2**(bi-1)
    seg=[0]*(2*bi2-1) #初期化。0のところに単位元を。
    for i in range(len(a)):
        seg[bi2+i-1]=a[i] #初期値代入
    #セグ木の構築は下から二段目から、順々に上の段へ
    for i in range(bi-1):
        for j in range(2**(bi-i-2)):
            b=2**(bi-i-2)-1+j
            #適宜minその他の関数で置換
            seg[b]=seg[2*b+1]+seg[2*b+2]
    return seg