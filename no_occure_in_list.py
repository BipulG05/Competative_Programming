# BIT MAGIC
# [5,3,4,5,6,3,6]
# every no occure twice 
# we have to find the number which no occure 1's time in list
# n^n = 0 so n^0=n

def finsingleoccur(arr):
    res = arr[0]
    no = []
    for i in range(1,len(arr)):
        res = res ^ arr[i]
    return res


t=int(input())
while t:
    arr = list(map(int,input().split()))
    print(finsingleoccur(arr))
    t -=1