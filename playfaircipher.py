def pure(word):
    list=[]
    for i in word:
        if i not in list:
            list.append(i);
    return list

def attach(list):
    alphabets=['a','b','c','d','e','f','g',
               'h','i','k','l','m','n',
               'o','p','q','r','s','t','u',
               'v','w','x','y','z']
    newlist=[]*25
    length=len(list)
    for i in range(length):
        newlist.append(list[i])

    for i in alphabets:
        if i not in list:
            newlist.append(i)

    return newlist

def matrix(list):
    k=0
    mat=[]*5
    
    for i in range(5):
        temp=[]*5
        for j in range(5):
            temp.append(list[k])
            k=k+1
        mat.append(temp)
    return mat
def findrow(list,letter):
    num=list.index(letter)
    return num%5
def findcol(list,letter):
    num=list.index(letter)
    return num/5
def checkrepeat(word):
    i=0
    while i<len(word):
        if word[i]==word[i+1]:
            word=word[:i+1]+'x'+word[i+1:]
        i=i+2
            
    return word
def checkword(word):
    if len(word)%2!=0:
        if word[-1]!='x':
            word=word+'x'
        else:
            word=word+'z'
    return word
def encryption(word,list,matrix):
    i1=0
    i2=0
    j1=0
    j2=0
    lett1=''
    lett2=''
    eword=''
    i=0
    while i<len(word):
       
        lett1=word[i]
        lett2=word[i+1]
        i1=findrow(list,lett1)
        i2=findcol(list,lett1)
        j1=findrow(list,lett2)
        j2=findcol(list,lett2)
        if(i1==j1):
            eword=eword+matrix[(i2+1)%5][i1]
            eword=eword+matrix[(j2+1)%5][j1]
        elif(i2==j2):
            eword=eword+matrix[i2][(i1+1)%5]
            eword=eword+matrix[j2][(j1+1)%5]
        else:
            eword=eword+matrix[j2][i1]
            eword=eword+matrix[i2][j1]
        i=i+2
    return eword
        
        
            
        
            
        
key='occurence'
list=pure(key)
new=attach(list)
##num=new.index('a')
##print num%5
##print num/5#division is col; modulo is row
new2=matrix(new)
print new2
##encry=str(raw_input('enter the key word to be encrypted'))
encry='talltrees'
encry=checkrepeat(encry)
encry=checkword(encry)

print encryption(encry,new,new2)


