from math import *
def getprime(n):
    prims = [True]*(n+1)
    # print(prims)
    prims[0]=False
    prims[1]=False
    for p in range(2,int(sqrt(n))+1):
        # print(p,(int(sqrt(n))+1))
        if prims[p] == True:
            for i in range(p*p,n+1,p):
                # print(p*p,n+1,p)
                prims[i]=False
    for i in range(0,len(prims)):
        if prims[i]==True:
            print(i,end=' ')

t=int(input())
while t:
    n=int(input())
    getprime(n)
    t -=1