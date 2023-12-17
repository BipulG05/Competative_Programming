# BIT MAGIC
# n -> input
# True/False -> output
# check if n is a powerof 2
# 512 -> True 512 = 2**9
# 1024 -> True 1024 = 2**10

def ispowerof(n): # T.C : O(1)
    if n<=0:
        return False
    x=n
    y=not(n & (n-1))
    return x and y

t=int(input())
while t:
    n=int(input())
    print(ispowerof(n))
    t -=1