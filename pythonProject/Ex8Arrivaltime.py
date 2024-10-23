def dep_arrvialtime(d,a):
    h1=int(d[0:2])
    h2=int(a[0:2])
    if h2==0:
        h2=24
    h=abs(h2-h1)*3600
    m=abs(int(a[3:5])-int(d[3:5]))*60
    s=abs(int(a[6:8])-int(d[6:8]))
    return h+m+s

print(dep_arrvialtime("04:01:00","11:30:00"))