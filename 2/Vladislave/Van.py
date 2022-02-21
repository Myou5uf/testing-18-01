import datetime

def calc(a,b):
    a = a.split('-')
    b = b.split('-')
    aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
    bb = datetime.date(int(b[0]), int(b[1]), int(b[2]))
    cc = abs(bb-aa)
    dd = str(cc)
    return (dd.split()[0])