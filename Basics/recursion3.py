#  to print all elements in list
def element(list,index):
    # index=0
    if(index==len(list)):
        return 0
    else:
        index+=1
        return list

list1=[1,2,3,4,5]
index=0
show=element(list1,index)
print(show)