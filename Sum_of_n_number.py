def sum1(n):
    # It's take time O(1)
    return((n*(n+1))//2)
def sum2(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return (sum)

print("sum of n number compatetive programming ",sum1(10))
print("sum of n number compatetive programming ",sum2(10))