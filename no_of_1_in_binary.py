# BIT MAGIC
# return's number of 1's in binary of an int
# 5 -> 101 ans = 2
# 7 -> 111 ans = 3

def Btcnbits(n):# T.C : O(log(n))
    cnt =0
    while n:
        cnt+=1
        n=n&(n-1)
    return cnt

def Bccnbits(n): # T.C : O(n) 
    s = str(bin(n))[2:]
    print('{}'.format(s))
    return s.count('1')

t=int(input())
while t:
    n=int(input())
    print(Btcnbits(n))
    print(Bccnbits(n))
    t -=1