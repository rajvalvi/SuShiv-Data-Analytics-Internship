# Pattern #9: Reverse Pattern of Digits from 10 
# Pattern:

# 1

# 3 2

# 6 5 4

# 10 9 8 7

def pattern(n):
    count=1
    # print("count1",count)
    for i in range(1,n):
        for j in range(count,count-i,-1):
            print(j,end=" ")
        k=i+1
        count=count+k
        # print("count",count)
        print()
n=5
pattern(n)