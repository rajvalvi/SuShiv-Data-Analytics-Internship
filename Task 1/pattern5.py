# Pattern #4: Inverted Pyramid of Descending Numbers
# Pattern:

# 5 5 5 5 5 

# 4 4 4 4 

# 3 3 3 

# 2 2 

# 1

def pattern(n):
    for i in range(n,0,-1):         #5
        for j in range(i):          #5*
            print(i,end=" ")        #onlny 5
        print()                     # space

n=5
pattern(n)