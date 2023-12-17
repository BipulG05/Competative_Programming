# It an Euclidean Algorithm : for more search google
# Time Complexity : O(log(min(a,b)))
# GCD and LCM of two number
def gcd(a,b):
    if a==0:
        return b
    #print(gcd(b%a,a))
    return gcd(b%a,a)
def lcm(a,b):
    p=a*b
    h=gcd(a,b)
    return(p//h)

t=int(input())
while t:
    n,m=map(int,input().split())
    print('gcd = {} lcm = {}'.format(gcd(n,m),lcm(n,m)))
    t=t-1