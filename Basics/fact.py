fact=1
# n=int(input("enter number:"))

def factorial(n):
    fact=1
    for i in range(1,6):
        fact*=i
    return fact

ans=factorial(5)
print(ans)
