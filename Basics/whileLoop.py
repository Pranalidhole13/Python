#que1
#print the numbers from 1 to 100
i=1
while i <= 5:
    # print(i)
    i+=1

#print from 100 to 1
j=100
while j>=1:
    # print(j)
    j-=1

#print the multiplication of n
# n=int(input("Enter number:"))
k=1
while k<=10:
    # print (n*k)
    k+=1

#print the elements from the following list
list=[1,4,9,16,25,36,49,64,81,100]
l=0
while l<len(list):
    # print(list[l])
    l+=1

#search for a number x in this list
num=[1,4,9,16,25,36,49,64,81,100]
key=int(input("Enter number to be search: "))
n=0
while n<len(num):
    if num[n]==key:
        print(n)
    n+=1