def pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(" ",end=" ")
        for k in range(n,i-1,-1):
            print("*",end=" ")
        print()
n=int(input("enter no of rows"))
pattern(n)