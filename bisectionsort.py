
##def bisec(L, e, low, high):
##    if high – low < 2:
##        return L[low] == e or L[high] == e
##    mid = low + int((high – low)/2)
##    if L[mid] == e:
##        return True 
##    if L[mid] > e:
##        return bSearch(L, e, low, mid – 1)
##    else: 
##        return bSearch(L, e, mid + 1, high)
##
##lis=[0,4,2,10,19,15,13]
##print bisec(lis,13,0,19)
##print 'this is new fiile'

import random 
g1 = 0 
g2 = 0 
mean = 100.0 
stdDev1 = 0.0 
stdDev2 = 20.0 
for i in range(1000): 
 g1 += random.gauss(mean, stdDev1) 
 g2 += random.gauss(mean, stdDev2) 

##print g1
##print g2
num6 = 0 
for test in range(10): 
 d = random.choice(range(10)) 
 if d == 6: 
     num6 += 1 
print num6



class Shape(object): 
 def __eq__(s1, s2): 
     return s1.area() == s2.area() 
 def __ge__(s1, s2): 
     return s1.area() >= s2.area() 
 
class Square(Shape): 
 def __init__(self, h): 
     self.side = float(h) 
 def area(self): 
     return self.side**2 
 def __str__(self): 
     return 'Square with side ' + str(self.side) 
 
class Circle(Shape): 
 def __init__(self, radius): 
     self.radius = radius 
 def area(self): 
     return 3.14159*(self.radius**2) 
 def __str__(self): 
     return 'Circle with radius ' + str(self.radius) 
 
def f(L): 
 if len(L) == 0: return None 
 x = L[0] 
 for s in L: 
     if s >= x: 
         x = s 
 return x 
 
##s = Square(4) 
##print s.area() 
##L = [] 
##shapes = {0:Circle, 1: Square} 
##for i in range(2): 
## L.append(shapes[i%2](i))#here i is there 4 constructor
####print L
##print L[0]
##print L[1] 
##print f(L)


import random
def cmpGuess(guess,maxVal):
    magicnumber=random.choice(range(maxVal))
    if (guess<magicnumber):
        return -1
    elif(guess==magicnumber):
        return 0
    else:
        return 1

def findNumber(maxVal):
    return random.choice(range(maxVal))

##print cmpGuess(findNumber(10),10)
for i in range(10):
    print i
for i in range(5):
    print i





















