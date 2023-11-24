# Pattern #10: Unique Pyramid Pattern of Digits
# Pattern:

# 1 

# 1 2 1 

# 1 2 3 2 1 

# 1 2 3 4 3 2 1 

# 1 2 3 4 5 4 3 2 1

def pattern(n):

    for i in range(1,n):
        for j in range(1,i):
            print(j,end=" ")

        for k in range(i,0,-1):
            print(k,end=" ")
        print()
            

n=5
pattern(n)