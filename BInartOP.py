# BIT MAGIC
# int to binary
def intTobinary(n):
    return(str(bin(n))[2:])

# binary to int
def binToint(s):
    return int(s,2)

# kth bit set from right: Ex : 5 ,1 it's 5 -> 101 here from left 101 have 1 so 'SET' 
# but if we take 5 ,2 5 -> 101 it's 2nd position from left is 0 so 'not set'
def kbit(n,k):
    print(str(bin(n))[2:])
    if n & (1 << (k-1)):
        print('SET')
    else:
        print('Not Set')
 

t=int(input())
while t:
    # n=int(input())
    # binary=intTobinary(n)
    # integr=binToint(binary)
    # print(n,binary,integr,n==integr)
    n,k=map(int,input().split())
    kbit(n,k)
    t -=1