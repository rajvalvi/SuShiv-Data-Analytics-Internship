# Pattern #7: Inverted Half Pyramid Number Pattern
# Pattern:

# 0 1 2 3 4 5 

# 0 1 2 3 4 

# 0 1 2 3 

# 0 1 2 

# 0 1

def pattern(no):
    for i in range(no,0,-1):
        for j in range(0,i+1):
            print(j,end=" ")
        print()

no=5
pattern(no)