# Pattern #8: Pyramid of Natural Numbers Less Than 10
# Pattern:

# 1 

# 2 3 4 

# 5 6 7 8 9

def pattern(n):
    count=1
    for i in range(n):              #0      :1
        for j in range(count):        #0+1=1  :1+1=2
            count+=1                #1      :
            print(count,end=" ")    #1
        print()
n=4
pattern(n)
