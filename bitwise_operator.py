# BIT MAGIC
# bitwise operators:- 'and':&  
# 'or':| 
# 'not':~ 
# 'xor':^ 
# 'right shift': >>  # it given no divided by power of 2^n (Ex:- no = 200 no>>3 =25 it's mean (2^3=8) 200//8=25) 
# 'left shift': <<   # it given no multiply by power of 2^n (Ex:- no = 200 no<<3 =1600 it's mean (2^3=8) 200*8=1600)

def mul(x,y):
    return x<<y
def div(x,y):
    return x>>y

def evenodd(n):
    if n&1==1:
        print('odd')
    else:
        print('even')

t=int(input())
while t:
    n=int(input())
    x,y=map(int,input().split())
    print(mul(x,y))
    print(div(x,y))
    evenodd(n)
    t -=1