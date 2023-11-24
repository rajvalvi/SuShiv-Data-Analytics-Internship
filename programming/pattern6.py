# Pattern #5: Inverted Pyramid of the Same Digit
# Pattern:

# 5 5 5 5 5 

# 5 5 5 5 

# 5 5 5 

# 5 5 

# 5

def pattern(n):
    space=1
    for i in range(n,0,-1):
        for k in range(space):
            print(" ",end="")
        space+=1

        for j in range(1,i+1):
            print(n,end=" ")
        print()
n=5
pattern(n)