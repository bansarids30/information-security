##def selSort(sro):
##    i=0
##    print 'here'
##    for i in range(len(sro) - 1):
##        print 'here2'
##        minIndx=i 
##        minVal=sro[i]
##        j = i + 1
##        while j < len(sro):
##            print 'here3'
##            if minVal > sro[j]:
##                minIndx = j
##                minVal= sro[j]
##            j =j+ 1 #here the infinite loop eas gong
##        temp = sro[i]
##        sro[i] = sro[minIndx]
##        sro[minIndx] = temp
##print 'hello'       
##lis=[0,3,4,6,9,2]
##selSort(lis)
##print lis
s='bansa'
total=0
list=['a','e','i','o','u']
for i in s:
    if i in list:
        total=total+1
print "Number of vowels"+str(total)
