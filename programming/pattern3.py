def pattern(n):
    count=1
    for i in range(n,0,-1):
        for j in range(i):
            print(count,end=" ")
        count+=1
        print()
n=5
pattern(n)