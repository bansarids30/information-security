numBuckets=47

def create():
    global numBuckets
    hset=[]
    for i in range(numBuckets):
        hset.append([])
    return hset

def hashElem(e):
    global numBuckets 
    return e%numBuckets 
 
def insert(hSet, i): 
    hSet[hashElem(i)].append(i) 
 
def remove(hSet, i): 
    newBucket = [] 
    for j in hSet[hashElem(i)]: 
        if j != i: 
            newBucket.append(j) 
    hSet[hashElem(i)] = newBucket 
 
def member(hSet, i): 
    return i in hSet[hashElem(i)] 

def test1(): 
    s = create() 
    for i in range(40): 
        insert(s, i) 
    insert(s, 325) 
    insert(s, 325) 
    insert(s, 987654321) 
    print s 
    print member(s, 325) 
    remove(s, 325) 
    print member(s, 325) 
    print member(s, 987654321) 
def hashElem(e): 
    global numBuckets 
    if type(e) == int: 
    val = e 
    if type(e) == str: 
 #Convert e to an int 
        val = 0 
        shift = 0 
    for c in e: 
        val = val + shift*ord(c) 
        shift += 1 
    return val%numBuckets 
def test2(): 
    d = create() 
    strs = ['ab', 'ba', '32a', 
    'big dog', 'small bird'] 
    for s in strs: 
        insert(d, s) 
    for i in range(40): 
        insert(d, i) 
    print d 
    print member(d, 'small bird') 
    print member(d, 'big bird') 
    remove(d, 'small bird') 
    print d 
test1()
test2()
