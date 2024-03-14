count=0
with open("no_ch.txt","r") as f:
    data=f.read()
    nums=data.split(",")
    print(type(nums))
    print(nums)
    for val in nums:
        if (int(val) %2==0):
            count +=1
print(count)