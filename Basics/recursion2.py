#sum of n natural numbers

def add(n):
    if(n==0):
        return 0
    # print(n)
    return add(n-1)+n

sum=(add(7))
print(sum)
