alpha={'a':0,'b':1,'c':2,'d':3,'e':4,
       'f':5,'g':6,'h':7,'i':8,'j':9,
       'k':10,'l':11,'m':12,'n':13,'o':14,
       'p':15,'q':16,'r':17,'s':18,'t':19,
       'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}
numer={0:'a',1:'b',2:'c',3:'d',4:'e',
       5:'f',6:'g',7:'h',8:'i',9:'j',
       10:'k',11:'l',12:'m',13:'n',14:'o',
       15:'p',16:'q',17:'r',18:'s',19:'t',
       20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}
       
def convertlist(word):
    list=[]
    for i in word:
        list.append(alpha[i])
    return list

def convertalpha(list):
    word=''
    for i in list:
        word=word+numer[i]
    return word

def checklen(word):
    if len(word)%3==1:
        word=word+'x'
    if len(word)%3==2:
        word=word+'x'+'y'
    return word

def tolist(list):
    num=len(list)/3
    k=0
    newlist=[]
    for i in range(num):
        temp=[]
        for j in range(3):
            temp.append(list[k])
            k=k+1
        newlist.append(temp)
    return newlist

    
def mul(matrix,list):
    newlist=[]
    num=0
    temp=[]
    for j in range(3):
        list1=list[0]
        print list1
        list=list[1:]
        for i in range(3):
            num=(list1[0]*matrix[i][0])+(list1[1]*matrix[i][1])+(list1[2]*matrix[i][2])
            num=num%26
            print num
            temp.append(num)
    return temp
key=[[17,7,5],[21,18,21],[2,2,19]]
list=[[15,0,24],[12,14,17],[15,0,24]]
lis=mul(key,list)
print convertalpha(lis)


    
