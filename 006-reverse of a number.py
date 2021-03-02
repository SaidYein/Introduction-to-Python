max=5
i=0
while i<max:
    sum=0
    j=max
    while j>i:
        sum=sum+j
        j=j-1
    print(sum)
    i=i+1
    