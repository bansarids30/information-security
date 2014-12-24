def generaterandom(m,a,c,x):
    for i in range(15):
        x=(a*x+c)%m
        print x
    
generaterandom(32,7,0,1)

def blumblumshub(x,p,q,s):
    n=p*q
    x=(s**2)%n
    list=[]
    for i in range(20):
        x=(x**2)%n
        b=x%2
        print 'x=',x
        print b
        list.append(b)
    print list
blumblumshub(1,383,503,101355)

