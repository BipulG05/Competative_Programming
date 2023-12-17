# Prime or Not 
# prime no has two factor is 1, nuber itself
# Approch one : O(n)
# Approch Two : Base Case + Hint O(1) -> O(root(n)) ( it's a best approch )
from math import *
def approch1(n): # Basic Approch
    divcnt = 0
    for i in range(1,n+1):
        if n%i==0:
            divcnt+=1
    #print(divcnt)
    if divcnt == 2 :
        return True
    return False

def approch2(n):
    if n==0 or n==1:# O(1)
        return False
    if n==2 or n==3:# O(1)
        return True
    if n%2==0 or n%3==0:# O(1)
        return False
    for i in range(5,int(sqrt(n))+1): # [1 - root(n)]
        if n%i==0 or n%(i+2)==0:
            return False
    return True

t=int(input())
while t:
    n=int(input())
    print(approch1(n))
    print(approch2(n))
    t -=1