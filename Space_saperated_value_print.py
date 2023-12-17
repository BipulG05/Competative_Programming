a=[1,2,3,4,5,6,7]
# method 1
for i in range(0,len(a)):
    print(a[i],end=' ')

# method 2
print('\n',*a)