def toshant(p,q):
    return (p-1)*(q-1)

def rsa(p,q,m):
    n=p*q
    tn=toshant(p,q)
    e=int(raw_input('enter num relatively prime to p & q'))
    d=(1*tn+1)/e
    print 'the public key is={',e,',',n,'}'
    print 'the private key is={',d,',',n,'}'
    c=0
    c=(m**e)%n
    print 'the cipher text is',c
    m2=(c**d)%n
    print 'the decrypteed text is',m2

p=17
q=11
plaintext=88
rsa(p,q,plaintext)
    
    
