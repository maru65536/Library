def nextday(y,m,d):
    a=[31,28,31,30,31,30,31,31,30,31,30,31]
    if d>=a[m-1]:
        if m==12:
            y+=1
            m,d=1,1
        elif m==2:
            if d==29:
                m+=1
                d=1
            else:
                if y%4==0 and y%100!=0 or y%400==0:
                    d+=1
                else:
                    m+=1
                    d=1
            
        else:
            m+=1
            d=1
    else:
        d+=1
    return y,m,d